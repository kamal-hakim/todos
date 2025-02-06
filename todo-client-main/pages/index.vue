<template>
  <Layout>
    <TodoList />
  </Layout>
</template>

<script>
import Layout from "../components/Layout.vue";
import TodoList from "../components/TodoList.vue";
export default {
  name: "IndexPage",
  components: { Layout, TodoList }
}
</script>