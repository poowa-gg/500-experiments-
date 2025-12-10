// Global state
let allExperiments = [];
let filteredExperiments = [];

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    loadSummary();
    loadFilters();
    loadExperiments();
    setupEventListeners();
});

// Load summary statistics
async function loadSummary() {
    try {
        const response = await fetch('/api/summary');
        const summary = await response.json();
        
        document.getElementById('total-experiments').textContent = summary.total_experiments;
        document.getElementById('avg-roi').textContent = summary.avg_expected_roi.toFixed(2) + 'x';
        document.getElementById('total-cost').textContent = '₦' + (summary.total_estimated_cost / 1000000).toFixed(1) + 'M';
        document.getElementById('high-priority').textContent = summary.high_priority_count;
    } catch (error) {
        console.error('Error loading summary:', error);
    }
}

// Load filter options
async function loadFilters() {
    try {
        const response = await fetch('/api/filters');
        const filters = await response.json();
        
        populateSelect('segment-filter', filters.segments, 'Segment');
        populateSelect('region-filter', filters.regions, 'Region');
        populateSelect('event-filter', filters.events, 'Event', true);
        populateSelect('channel-filter', filters.channels, 'Channel', true);
        populateSelect('priority-filter', filters.priorities, 'Priority');
    } catch (error) {
        console.error('Error loading filters:', error);
    }
}

// Populate select dropdown
function populateSelect(id, options, label, formatUnderscore = false) {
    const select = document.getElementById(id);
    options.sort().forEach(option => {
        const opt = document.createElement('option');
        opt.value = option;
        opt.textContent = formatUnderscore ? 
            option.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase()) : 
            option.charAt(0).toUpperCase() + option.slice(1);
        select.appendChild(opt);
    });
}

// Load experiments
async function loadExperiments() {
    const params = new URLSearchParams({
        segment: document.getElementById('segment-filter').value,
        region: document.getElementById('region-filter').value,
        event: document.getElementById('event-filter').value,
        channel: document.getElementById('channel-filter').value,
        priority: document.getElementById('priority-filter').value,
        sort: document.getElementById('sort-filter').value,
        order: 'desc'
    });
    
    try {
        const response = await fetch(`/api/experiments?${params}`);
        const experiments = await response.json();
        
        allExperiments = experiments;
        filteredExperiments = experiments;
        displayExperiments(experiments);
    } catch (error) {
        console.error('Error loading experiments:', error);
    }
}

// Display experiments
function displayExperiments(experiments) {
    const container = document.getElementById('experiments-list');
    const countElement = document.getElementById('results-count');
    
    countElement.textContent = `Showing ${experiments.length} experiments`;
    
    if (experiments.length === 0) {
        container.innerHTML = '<p style="text-align: center; color: #999; padding: 40px;">No experiments found matching your filters.</p>';
        return;
    }
    
    container.innerHTML = experiments.map(exp => `
        <div class="experiment-card" onclick="showExperimentDetails('${exp.experiment_id}')">
            <div class="experiment-header">
                <span class="experiment-id">${exp.experiment_id}</span>
                <span class="priority-badge priority-${exp.priority}">${exp.priority}</span>
            </div>
            
            <div class="experiment-meta">
                <div class="meta-item">
                    <span class="meta-label">Segment:</span>
                    <span class="meta-value">${exp.user_segment.charAt(0).toUpperCase() + exp.user_segment.slice(1)}</span>
                </div>
                <div class="meta-item">
                    <span class="meta-label">Region:</span>
                    <span class="meta-value">${exp.region}</span>
                </div>
                <div class="meta-item">
                    <span class="meta-label">Event:</span>
                    <span class="meta-value">${exp.climate_event.replace(/_/g, ' ')}</span>
                </div>
                <div class="meta-item">
                    <span class="meta-label">Channel:</span>
                    <span class="meta-value">${exp.alert_channel.replace(/_/g, ' ')}</span>
                </div>
            </div>
            
            <div class="experiment-hypothesis">
                "${exp.hypothesis}"
            </div>
            
            <div class="experiment-stats">
                <div class="stat-item">
                    <span class="stat-item-label">ROI</span>
                    <span class="stat-item-value">${exp.expected_roi}x</span>
                </div>
                <div class="stat-item">
                    <span class="stat-item-label">Cost</span>
                    <span class="stat-item-value">₦${(exp.cost_estimate_ngn / 1000).toFixed(0)}k</span>
                </div>
                <div class="stat-item">
                    <span class="stat-item-label">Sample</span>
                    <span class="stat-item-value">${exp.sample_size.toLocaleString()}</span>
                </div>
                <div class="stat-item">
                    <span class="stat-item-label">Duration</span>
                    <span class="stat-item-value">${exp.duration_days}d</span>
                </div>
            </div>
        </div>
    `).join('');
}

// Show experiment details in modal
async function showExperimentDetails(expId) {
    try {
        const response = await fetch(`/api/experiment/${expId}`);
        const exp = await response.json();
        
        const modalBody = document.getElementById('modal-body');
        modalBody.innerHTML = `
            <h2>${exp.experiment_id}</h2>
            <span class="priority-badge priority-${exp.priority}">${exp.priority} Priority</span>
            
            <div class="modal-section">
                <h3>Overview</h3>
                <div class="modal-grid">
                    <div class="modal-item">
                        <div class="modal-item-label">User Segment</div>
                        <div class="modal-item-value">${exp.user_segment.charAt(0).toUpperCase() + exp.user_segment.slice(1)}</div>
                    </div>
                    <div class="modal-item">
                        <div class="modal-item-label">Region</div>
                        <div class="modal-item-value">${exp.region}</div>
                    </div>
                    <div class="modal-item">
                        <div class="modal-item-label">Climate Event</div>
                        <div class="modal-item-value">${exp.climate_event.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</div>
                    </div>
                    <div class="modal-item">
                        <div class="modal-item-label">Alert Channel</div>
                        <div class="modal-item-value">${exp.alert_channel.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</div>
                    </div>
                </div>
            </div>
            
            <div class="modal-section">
                <h3>Hypothesis</h3>
                <p style="font-style: italic; color: #555;">"${exp.hypothesis}"</p>
            </div>
            
            <div class="modal-section">
                <h3>Recommended Action</h3>
                <p><strong>${exp.recommended_action.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</strong></p>
            </div>
            
            <div class="modal-section">
                <h3>Experiment Parameters</h3>
                <div class="modal-grid">
                    <div class="modal-item">
                        <div class="modal-item-label">Sample Size</div>
                        <div class="modal-item-value">${exp.sample_size.toLocaleString()} users</div>
                    </div>
                    <div class="modal-item">
                        <div class="modal-item-label">Duration</div>
                        <div class="modal-item-value">${exp.duration_days} days</div>
                    </div>
                    <div class="modal-item">
                        <div class="modal-item-label">Forecast Horizon</div>
                        <div class="modal-item-value">${exp.forecast_horizon.replace(/_/g, ' ')}</div>
                    </div>
                    <div class="modal-item">
                        <div class="modal-item-label">Lead Time</div>
                        <div class="modal-item-value">${exp.lead_time_hours} hours</div>
                    </div>
                    <div class="modal-item">
                        <div class="modal-item-label">Predicted Accuracy</div>
                        <div class="modal-item-value">${(exp.predicted_accuracy * 100).toFixed(0)}%</div>
                    </div>
                    <div class="modal-item">
                        <div class="modal-item-label">ML Model</div>
                        <div class="modal-item-value">${exp.ml_model.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</div>
                    </div>
                </div>
            </div>
            
            <div class="modal-section">
                <h3>Financial</h3>
                <div class="modal-grid">
                    <div class="modal-item">
                        <div class="modal-item-label">Cost Estimate</div>
                        <div class="modal-item-value">₦${exp.cost_estimate_ngn.toLocaleString()}</div>
                    </div>
                    <div class="modal-item">
                        <div class="modal-item-label">Expected ROI</div>
                        <div class="modal-item-value">${exp.expected_roi}x</div>
                    </div>
                </div>
            </div>
            
            <div class="modal-section">
                <h3>Success Metrics</h3>
                <div class="tag-list">
                    ${exp.success_metrics.map(m => `<span class="tag">${m.replace(/_/g, ' ')}</span>`).join('')}
                </div>
            </div>
            
            <div class="modal-section">
                <h3>Data Sources</h3>
                <div class="tag-list">
                    ${exp.data_sources.map(s => `<span class="tag">${s.replace(/_/g, ' ')}</span>`).join('')}
                </div>
            </div>
            
            <div class="modal-section">
                <h3>Validation Method</h3>
                <p>${exp.validation_method.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}</p>
            </div>
        `;
        
        document.getElementById('modal').style.display = 'block';
    } catch (error) {
        console.error('Error loading experiment details:', error);
    }
}

// Setup event listeners
function setupEventListeners() {
    // Filter changes
    document.querySelectorAll('.filter-select').forEach(select => {
        select.addEventListener('change', loadExperiments);
    });
    
    // Reset filters
    document.getElementById('reset-filters').addEventListener('click', () => {
        document.querySelectorAll('.filter-select').forEach(select => {
            if (select.id !== 'sort-filter') {
                select.value = '';
            }
        });
        loadExperiments();
    });
    
    // Modal close
    document.querySelector('.close').addEventListener('click', () => {
        document.getElementById('modal').style.display = 'none';
    });
    
    window.addEventListener('click', (event) => {
        const modal = document.getElementById('modal');
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
}
