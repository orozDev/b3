const content = document.getElementById('content')
const btn = document.getElementById('btn')

btn.addEventListener('click', () => {
    content.innerHTML = '<div class="text-center"><img width="30px" src="https://i.gifer.com/ZKZg.gif"></div>'
    fetch('https://jsonplaceholder.typicode.com/todos/').
    then(res => {
        return res.json()
    })
    .then(res => {
        return new Promise((resolve, reject) => {
            setTimeout(() => resolve(res), 4000)
        })
    })
    .then(res => {
        console.log(res)
        res.splice(0, 70)
        content.innerHTML = ''
        res.forEach((item, idx) => {
            content.innerHTML += `
            <div class="col-lg-3 col-md-4 col-sm-6 col-12">
                <div class="card">
                    <img src="https://picsum.photos/200/" class="card-img-top" alt="...">
                    <div class="card-body">
                    <h5 class="card-title">${item.title}</h5>
                    </div>
                </div>
            </div>
            `
        })
    })
})