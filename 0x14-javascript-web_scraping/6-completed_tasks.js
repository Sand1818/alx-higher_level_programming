#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, resopnse, body) => {
  if (error) console.log(error);
  else {
    const Completed_tasks = {};
    const todos = JSON.parse(body);
    for (const todo of todos) {
      if (todo.completed) {
        if (todo.userId in Completed_tasks) {
          Completed_tasks[todo.userId]++;
        } else {
          Completed_tasks[todo.userId] = 1;
        }
      }
    }
    console.log(Completed_tasks);
  }
});
