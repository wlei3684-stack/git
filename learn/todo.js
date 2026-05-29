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

function clearDone() {
  const remaining = todos.filter(t => !t.done);
  todos.length = 0;
  todos.push(...remaining);
}

function findByKeyword(keyword) {
  return todos.filter(t => t.task.includes(keyword));
}

// 示例
add("学 Git");
add("学 Python");
add("学 JavaScript");
done(0);
done(1);
console.log("全部:");
list();
console.log("---");
console.log("搜索 'Git':", findByKeyword("Git"));
