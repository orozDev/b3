const createTaskForm = document.forms.createTaskForm
const taskContainer = document.querySelector('#taskContainer')
const createTaskFormModal = document.querySelector('#createTaskModal');
const modal = new bootstrap.Modal(createTaskFormModal)
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


const tasks = [
    new Task({
        name: 'oroz',
        desc: 'sadas dasd asd as',
        deadline: new Date('2023-12-12'),
        isCompleted: true
    }),
    new Task({
        name: 'nursultan',
        desc: 'sadas dasd asd as',
        deadline: new Date('2020-12-12'),
        isCompleted: true
    }),
    new Task({
        name: 'bahrom',
        desc: 'sadas dasd asd as',
        deadline: new Date('2020-12-12'),
        isCompleted: true
    }),
    new Task({
        name: 'zdsasdas',
        desc: 'sadas dasd asd as',
        deadline: new Date('2020-12-12'),
        isCompleted: true
    }),
    new Task({
        name: 'zdsasdas',
        desc: 'sadas dasd asd as',
        deadline: new Date('2020-12-12'),
        isCompleted: true
    }),
]


const makeTemplate = ({
    id, name, desc, deadline, isCompleted
}) => `
    <tr>
        <th scope="row">${id}</th>
        <td>${name}</td>
        <td><p> ${desc}</p></td>
        <td><p> ${deadline.toDateString()}</p></td>
        <td><input type="checkbox" ${isCompleted ? 'checked' : ''}" name=""></td>
        <td>
            <div class="d-flex gap-3">
                <button class="btn btn-sm btn-warning"><i
                        class="fa-solid fa-pen-to-square"></i></button>
                <button class="btn btn-sm btn-danger"><i class="fa-solid fa-trash"></i></button>
            </div>
        </td>
    </tr>
    `

const renderTasks = (listOfTasks) => {
    taskContainer.innerHTML = ''
    for (const task of listOfTasks) {
        taskContainer.innerHTML += makeTemplate(task)
    }
}    

createTaskForm.addEventListener('submit', e => {
    e.preventDefault();

    const name = createTaskForm.name.value
    const desc = createTaskForm.desc.value
    const deadline = new Date(createTaskForm.deadline.value)

    tasks.push(new Task({
        name, desc, deadline: new Date(deadline), isCompleted: false,
    }))

    console.log(tasks);
    
    taskContainer.innerHTML += makeTemplate(tasks.at(-1))

    modal.hide();
    createTaskForm.reset()
    
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