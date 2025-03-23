<template>
  <v-container>
    <v-btn class="mb-4" color="primary" @click="openCreateModal">
      Create User
    </v-btn>

    <DynamicTable :items="users" :headers="tableHeaders">
      <!-- Slot for the actions column (Edit and Delete) -->
      <template #actions="{ item }">
        <v-btn icon small @click="openEditModal(item)">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
        <v-btn icon small @click="confirmDelete(item)">
          <v-icon>mdi-delete</v-icon>
        </v-btn>
      </template>
    </DynamicTable>
  </v-container>
</template>

<script>
import { ref, onMounted } from 'vue'
import userService from '../services/userService'
import DynamicTable from '../components/ui/DynamicTable.vue'

export default {
  name: 'Main',
  components: { DynamicTable },
  setup() {
    const users = ref([])

    const formatDate = (timestamp) => {
      const date = new Date(timestamp * 1000)
      const pad = (num) => num.toString().padStart(2, '0')
      return `${pad(date.getMonth() + 1)}/${pad(date.getDate())}/${date.getFullYear()} ${pad(date.getHours())}:${pad(date.getMinutes())}:${pad(date.getSeconds())}`
    }
    const tableHeaders = ref([
      { field: 'username', label: 'Username' },
      { 
        field: 'roles', 
        label: 'Roles', 
        render: (item) => Array.isArray(item.roles) ? item.roles.join(', ') : item.roles 
      },
      { field: 'preferences.timezone', label: 'Timezone' },
      { 
        field: 'active', 
        label: 'Is Active?', 
        render: (item) => item.active ? 'Yes' : 'No'
      },
      { field: 'updated_ts', label: 'Last Updated At', render: (item) => formatDate(item.updated_ts) },
      { field: 'created_ts', label: 'Created At', render: (item) => formatDate(item.created_ts) }
    ])

    const fetchUsers = async () => {
      try {
        const response = await userService.listUsers()
        users.value = Array.isArray(response.data)
          ? response.data
          : response.data.users || []
      } catch (error) {
        console.error('Error fetching users:', error)
      }
    }

    const openCreateModal = () => {
      // Logic to open the create user modal
    }

    const openEditModal = (user) => {
      // Logic to open the edit user modal
    }

    const confirmDelete = async (user) => {
      if (confirm(`Are you sure you want to delete the user ${user.username}?`)) {
        try {
          await userService.deleteUser(user._id.$oid)
          fetchUsers()
        } catch (error) {
          console.error('Error deleting user:', error)
        }
      }
    }

    onMounted(fetchUsers)

    return {
      users,
      tableHeaders,
      openCreateModal,
      openEditModal,
      confirmDelete
    }
  }
}
</script>
