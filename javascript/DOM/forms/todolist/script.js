const createTaskForm = document.forms.createTaskForm
const taskContainer = document.querySelector('#taskContainer')
const createTaskFormModal = document.querySelector('#createTaskModal');
const modal = new bootstrap.Modal(createTaskFormModal)
const updateTaskHtmlModal = document.querySelector('#updateTaskModal');
const updateTaskModal = new bootstrap.Modal(updateTaskHtmlModal)
const searchInput = document.querySelector('#searchInput');

let taskId = 1

class Task {
    constructor({name, desc, deadline, isCompleted}) {
        this.id = taskId
        this.name = name
        this.desc = desc
        this.deadline = deadline
        this.isCompleted = isCompleted
        taskId++
    }

}


const tasks = JSON.parse(localStorage.getItem('tasks') ?? '[]')

console.log(tasks)

//     [
//     new Task({
//         name: 'oroz',
//         desc: 'sadas dasd asd as',
//         deadline: new Date('2023-12-12'),
//         isCompleted: true
//     }),
//     new Task({
//         name: 'nursultan',
//         desc: 'sadas dasd asd as',
//         deadline: new Date('2020-12-12'),
//         isCompleted: true
//     }),
//     new Task({
//         name: 'bahrom',
//         desc: 'sadas dasd asd as',
//         deadline: new Date('2020-12-12'),
//         isCompleted: false
//     }),
//     new Task({
//         name: 'zdsasdas',
//         desc: 'sadas dasd asd as',
//         deadline: new Date('2020-12-12'),
//         isCompleted: false
//     }),
//     new Task({
//         name: 'zdsasdas',
//         desc: 'sadas dasd asd as',
//         deadline: new Date('2020-12-12'),
//         isCompleted: true
//     })
// ]


const makeTemplate = ({
                          id, name, desc, deadline, isCompleted
                      }) => `
    <tr id="task_${id}">
        <th scope="row">${id}</th>
        <td>${name}</td>
        <td><p> ${desc}</p></td>
        <td><p> ${new Date(deadline).toLocaleDateString()}</p></td>
        <td><input type="checkbox" onchange="toggleDoneTask(${id})" ${isCompleted ? 'checked' : ''} name=""></td>
        <td>
            <div class="d-flex gap-3">
                <button class="btn btn-sm btn-warning" onclick="preparingToUpdate(${id})"><i
                        class="fa-solid fa-pen-to-square"></i></button>
                <button class="btn btn-sm btn-danger" onclick="deleteTask(${id})"><i class="fa-solid fa-trash"></i></button>
            </div>
        </td>
    </tr>
    `

const reloadData = () => {
    localStorage.setItem('tasks', JSON.stringify(tasks))
}

const renderTasks = (listOfTasks) => {
    taskContainer.innerHTML = ''
    for (const task of listOfTasks) {
        taskContainer.innerHTML += makeTemplate(task)
    }
}

const deleteTask = (taskId) => {
    const taskIndex = tasks.findIndex(item => item.id === taskId)
    tasks.splice(taskIndex, 1)
    reloadData()
    document.querySelector(`#task_${taskId}`).remove()

}

const toggleDoneTask = (taskId) => {
    const task = tasks.find(item => item.id === taskId)
    task.isCompleted = !task.isCompleted
    reloadData()
    console.log(tasks)
}

const preparingToUpdate = (taskId) => {
    updateTaskModal.show()

    const task = tasks.find(item => item.id === taskId)

    const updateTaskForm = document.forms.updateTaskForm
    updateTaskForm.name.value = task.name
    updateTaskForm.desc.value = task.desc
    updateTaskForm.deadline.value = task.deadline.slice(0, 10)
    updateTaskForm.setAttribute('data-task_id', taskId)

}


createTaskForm.addEventListener('submit', e => {
    e.preventDefault();

    const name = createTaskForm.name.value
    const desc = createTaskForm.desc.value
    const deadline = new Date(createTaskForm.deadline.value).toISOString()

    tasks.push(new Task({
        name, desc, deadline, isCompleted: false,
    }))
    reloadData()

    console.log(tasks);

    taskContainer.innerHTML += makeTemplate(tasks.at(-1))

    modal.hide();
    createTaskForm.reset()

})

const updateTaskForm = document.forms.updateTaskForm

updateTaskForm.addEventListener('submit', e => {
    e.preventDefault()

    const taskId = +updateTaskForm.dataset.task_id

    const task = tasks.find(item => item.id === taskId)

    task.name = updateTaskForm.name.value
    task.desc = updateTaskForm.desc.value
    task.deadline = new Date(updateTaskForm.deadline.value).toISOString()
    reloadData()

    updateTaskModal.hide()
    updateTaskForm.reset()

    renderTasks(tasks)

})

searchInput.addEventListener('input', e => {

    const val = e.target.value
    const serchedTasks = tasks.filter(task => task.name.includes(val))
    renderTasks(serchedTasks)

})

const start = () => {
    taskContainer.innerHTML = `<tr><td colspan="6" align="center"><img src="./loading.gif"></td></tr>`
    setTimeout(() => {
        renderTasks(tasks)
    }, 1000)

}

start()