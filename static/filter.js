function addFilterItem() {
    const div = document.createElement('div');

    div.className = 'search-item';
    
    currContent = document.getElementById('current_search_item').value

    div.innerHTML = '<p>' + currContent + '</p>' ;
    document.getElementById('search_box').appendChild(div);
    console.log('working')
}