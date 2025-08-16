var productContainer = document.getElementById("products")
var search = document.getElementById("search")
var productlist = productContainer.querySelectorAll("div")

search.addEventListener("keyup",(event)=>{
    var enteredValue = event.target.value.toUpperCase()

    for (let i = 0; i < productlist.length; i++) {
        const getValue = productlist[i].querySelector('p').textContent

        if (getValue.toUpperCase().indexOf(enteredValue) < 0) {
            productlist[i].style.display="none"
        }
        
    }
})