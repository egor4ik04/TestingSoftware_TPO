const input = document.getElementById('taskInput');
const addBtn = document.getElementById('addBtn');
const list = document.getElementById('taskList');
const allBtn = document.getElementById('allBtn');
const activeBtn = document.getElementById('activeBtn');
const doneBtn = document.getElementById('doneBtn');

let tasks = []; 
// #3 Список задач не сохраняется при обновлении страницы: не сохраняется в localStorage — всё теряется при перезагрузке

function renderTasks(filter = "all") {
  list.innerHTML = "";
  tasks.forEach(task => {
    if (filter === "active" && task.done) return;
    if (filter === "done" && !task.done) return;

    const li = document.createElement('li');
    li.textContent = task.text;
    if (task.done) li.classList.add('done');

    const toggleBtn = document.createElement('button');
    toggleBtn.textContent = "Переключить";
    toggleBtn.onclick = () => {
      task.done = !task.done;
      renderTasks(filter);
    };

    const delBtn = document.createElement('button');
    delBtn.textContent = "Удалить";
    delBtn.onclick = () => {
      tasks = tasks.filter(t => t !== task);
      renderTasks(filter);
    };

    li.appendChild(toggleBtn);
    li.appendChild(delBtn);
    list.appendChild(li);
  });
}

addBtn.onclick = () => {
  // #1 Добавляется пустая задача: нет проверки на пустую строку
  tasks.push({ text: input.value, done: false });
  input.value = "";
  renderTasks();
// #2 Фильтр не сохраняется при добавлении задачи: при добавлении — всегда сбрасывается на "все"
};

allBtn.onclick = () => renderTasks("all");
activeBtn.onclick = () => renderTasks("active");
doneBtn.onclick = () => renderTasks("dane");
// #4 Фильтр “Выполненные” отображает все задачи: фильтр показывает все задачи из-за ошибки в параметре

renderTasks();
