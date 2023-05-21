fetch("../partial/_nav.html")
  .then(response => {
    return response.text()
  })
  .then(data => {
    
    document.querySelector("header").innerHTML = data;

    nav_brand = $('#logo')

    // Active Link
    var path = window.location.pathname.split("/").pop();
    if (path == ''){
        path = 'index.html';
    }

    // var target = $('ul li a[href="'+path+'"]');
    var target = $("a[href$='"+path+"']");
    target.addClass('active');

    console.log(nav_brand);
    nav_brand.removeClass('active');
});


fetch("../partial/_footer.html")
.then(response => {
  return response.text()
})
.then(data => {
  document.querySelector("footer").innerHTML = data;

  let web_date = document.getElementById("date");
  const d = new Date();
  let year = d.getFullYear();
  web_date.innerHTML = "&copy; " + year + " Gabriel. All Rights Reserved.";
  web_date.style.color = "#fff";
});
