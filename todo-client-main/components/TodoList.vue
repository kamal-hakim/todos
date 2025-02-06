<template>
  <div class="w-full max-w-xl p-4 bg-white border border-gray-200 rounded-lg shadow-lg lg:p-8 dark:bg-gray-800 dark:border-gray-700">
    <h1 class="title">Your To Do List</h1>
    <div class="flex items-center justify-between mb-8">
      <div class="w-full">   
        <label for="default-search" class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>
        <div class="relative">
            <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                </svg>
            </div>
            <input type="search" v-model="searchQuery" placeholder="Search" class="block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"/>
        </div>
        <div class="relative">
            <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
              <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                <path fill-rule="evenodd" d="M18 5.05h1a2 2 0 0 1 2 2v2H3v-2a2 2 0 0 1 2-2h1v-1a1 1 0 1 1 2 0v1h3v-1a1 1 0 1 1 2 0v1h3v-1a1 1 0 1 1 2 0v1Zm-15 6v8a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-8H3ZM11 18a1 1 0 1 0 2 0v-1h1a1 1 0 1 0 0-2h-1v-1a1 1 0 1 0-2 0v1h-1a1 1 0 1 0 0 2h1v1Z" clip-rule="evenodd"/>
              </svg>
            </div>
            <input type="text" placeholder="Add your new task" v-model="newTodoText" @keyup.enter="handleAddToDo" class="block w-full mt-4 p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
        </div>
      </div>
    </div>
    <div class="flex-row flex">
      <div class="filters flex-col items-start">
        <button class="filterBtn" :class="{ filterActive: filter === undefined }"
          @click="handleFilterChange()">All</button>
        <button class="filterBtn" :class="{ filterActive: filter === false }"
          @click="handleFilterChange(false)">Active</button>
        <button class="filterBtn" :class="{ filterActive: filter === true }"
          @click="handleFilterChange(true)">Completed</button>
      </div>
      <div class="w-full">
        <p class="m20" v-if="$fetchState.pending">Retrieving list of To Do ...</p>
        <p class="m20" v-else-if="$fetchState.error">Error retrieving list of To Do</p>
        <div v-else>
          <div class="toDoRow" v-for="todo of filteredItems" :key="todo.id">
            <Todo :todo="todo" @onChange="handleChange" @onDelete="handleDelete" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { debounce } from 'lodash'
import Todo from './Todo.vue'

export default {
  data() {
    return {
    todos: [],
    newTodoText: '',
    filter: undefined,
    searchQuery: ''
  }},
  async fetch() {
    let path = 'todos'
    if (this.filter !== undefined) {
      path += `?completed=${this.filter}`
    }
    this.todos = await fetch(`${this.$config.apiURL}/${path}`)
      .then(res => res.json());
  },
  methods: {
    async handleAddToDo() {
      if(this.newTodoText !== '') {
        const todo = { description: this.newTodoText, complete: false };
        const res = await fetch(`${this.$config.apiURL}/todos`, {
          method: "POST",
          body: JSON.stringify(todo),
          headers: {
            'Content-Type': 'application/json'
          }
        });
        const json = await res.json();
        this.todos.push(json);
        this.newTodoText = ''
      }
    },
    handleChange: debounce(async function (todo) {
      await fetch(`${this.$config.apiURL}/todos/${todo.id}`, {
        method: "PUT",
        body: JSON.stringify(todo),
        headers: {
          'Content-Type': 'application/json'
        }
      });
    }, 500),
    async handleDelete(todo) {
      await fetch(`${this.$config.apiURL}/todos/${todo.id}`, {
        method: "DELETE"
      });
      const idx = this.todos.findIndex((t) => t.id === todo.id)
      this.todos = this.todos.splice(idx, 1)
    },
    handleFilterChange(value) { 
      this.filter = value
      this.$fetch()
    }
  },
  computed: {
     filteredItems() {
      return this.todos.filter(todo =>todo.description.toLowerCase().includes(this.searchQuery.toLowerCase()))
    }
  },
  components: { Todo }
}
</script>

<style>

.filters {
  display: flex;
  padding: 20px;
  border-top: 1px solid black;
}

.filterBtn {
  background: none;
  border: none;
  cursor: pointer;
}

.filterActive {
  text-decoration: underline;
}

.m20 {
  margin: 20px;
}
</style>
