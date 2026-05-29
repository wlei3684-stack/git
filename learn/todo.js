const todos = [];

function add(task) {
  todos.push({ task, done: false });
}

function done(index) {
  if (todos[index]) todos[index].done = true;
}

function list() {
  todos.forEach((t, i) => {
    const status = t.done ? "✓" : "○";
    console.log(`${i}: ${status} ${t.task}`);
  });
}

// 示例
add("学 Git");
add("学 Python");
done(0);
list();
