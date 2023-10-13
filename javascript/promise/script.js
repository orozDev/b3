// console.log(1)
// setTimeout(() => {
//     console.log('Time has finished')
//     console.log(2)
//     setTimeout(() => {
//         console.log('Time has finished 2')
//         console.log(3)
//     }, 2000)
    
// }, 2000)

console.log('Requesting data from server...')

const firstRequest = new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log('Data received from server')
        const option = prompt(
            `Select action:
                1) Ok
                2) Error
            `, 
            1
        )

        if (option == 2) {
            reject('ERROR')
        }
        
        const data = '{"body": "data ...sdfv sdfsd", "status": 200}'
        resolve(data)
    }, 2000)
})

firstRequest.then(res => {
    console.log('Preparing data...')
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const data = JSON.parse(res)
            resolve(data)
        }, 2000)
    })
})
.catch((error) => {
    console.log(error)
    return new Promise((resolve, reject) => reject(error))
})
.then(res => {
    console.log(res)
})
.finally(errOrRes => {
    console.log('FINAL')
})
