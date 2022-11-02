function addFilterItem() {
    const div = document.createElement('div');

    div.className = 'search-item';
    
    currContent = document.getElementById('current_search_item').value

    div.innerHTML = '<p>' + currContent + '</p>' ;
    document.getElementById('search_box').appendChild(div);
    
    cookie = getCookie("filterStr")

    console.log(cookie)

    if (cookie == "" || cookie == null) {
        var date = new Date();
        date.setDate(date.getDate() + 1);
        string = ""
        string += currContent + ';'
        document.cookie = "filterStr=" + string + '; expires=' + date
    }
    else {
        string += currContent + ';'
        document.cookie = "filterStr=" + string
    } 
}
 
function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }

function delete_cookie() {
    document.cookie = 'filterStr=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}
  