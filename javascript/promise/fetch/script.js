const sleep = (seconds) => new Promise(res => setTimeout(res, seconds * 1000))


const start = async () => {
    const postContainer = document.querySelector('#posts')
    postContainer.innerHTML = '<div class="col-12 text-center"><img src="https://i.gifer.com/ZKZg.gif" width="40px"></div>'

    await sleep(2)
    const response = await fetch('https://jsonplaceholder.typicode.com/posts')

    if (response.ok) {
        const posts = await response.json()
        postContainer.innerHTML = ''
        for (const post of posts) {
            postContainer.innerHTML += `
                <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-4">
                    <div class="card h-100">
                      <div class="card-body">
                        <h5 class="card-title">${post.id}. ${post.title}</h5>
                        <p class="card-text">${post.body}</p>
                      </div>
                    </div>
                </div>
            `
        }
    }

}

start()