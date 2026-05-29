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

function remove(index) {
  todos.splice(index, 1);
}

function clear() {
  todos.length = 0;
}

// 示例
add("学 Git");
add("学 Python");
add("学 JavaScript");
done(0);
done(1);
remove(2);
list();
console.log(`共 ${todos.length} 条`);
