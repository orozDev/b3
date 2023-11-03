const createTaskForm = document.forms.createTaskForm
const taskContainer = document.querySelector('#taskContainer')
const createTaskFormModal = document.getElementById('createTaskModal');
const modal = bootstrap.Modal.getInstance(createTaskFormModal)


let taskId = 1

const makeTemplate = ({
    id, name, desc, isCompleted
}) => `
    <tr>
        <th scope="row">${id}</th>
        <td>${name}</td>
        <td><p> ${desc}</p></td>
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


createTaskForm.addEventListener('submit', e => {
    e.preventDefault();

    const name = createTaskForm.name.value
    const desc = createTaskForm.desc.value
    const deadline = new Date(createTaskForm.deadline.value)

    taskContainer.innerHTML += makeTemplate({taskId, name, desc, deadline})
    taskId++
    modal.hide();
    
})


/*
    let taskId = 1

class Task {
    constructor({
        name, desc, isCompleted
    }) {
        this.id = taskId
        this.name = name
        this.desc = desc
        this.isCompleted = isCompleted
        taskId++
    }
}

const tasks = [
    new Task({
        name: 'sadas',
        desc: ''
    })
]

*/