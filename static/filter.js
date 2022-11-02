function addFilterItem() {
    const div = document.createElement('div');

    div.className = 'search-item';
    
    currContent = document.getElementById('current_search_item')

    div.innerHTML = currContent;
}