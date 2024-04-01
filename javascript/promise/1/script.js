const sleep = (seconds) => {
    return new Promise((res, rej) => setTimeout(() => res(), seconds))
}

const requestData = () => {
    return new Promise((resolve, reject) => {
        sleep(3000).then(() => {
            const now = new Date()
            const min = now.getMinutes()
            if (min % 2 === 0) resolve({
                status: 200,
                data: {
                    user: 1,
                    email: 'oroz@gmail.com'
                }
            })
            else reject({error: 'Network error !'})
        })
    })
}

console.log('start')

const start = () => {
    requestData().then(data => {
        console.log(data)
    }).catch(err => {
        console.log(err)
    })
    console.log(1)
    console.log(2)
    console.log(2)
    console.log(2)
    console.log(2)
    console.log(2)
}

start()

console.log('end')