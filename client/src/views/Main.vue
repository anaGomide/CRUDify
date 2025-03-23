<template>
  <v-container>
    <v-btn class="mb-4" color="primary" @click="openCreateModal">
      Create User
    </v-btn>

    <DynamicTable :items="users" :headers="tableHeaders">
      <!-- Slot for the actions column (Edit and Delete) -->
      <template #actions="{ item }">
        <v-icon color="green" class="action-icon" @click="openEditModal(item)">
          mdi-pencil
        </v-icon>

        <v-icon color="red" class="action-icon" @click="confirmDelete(item)">
          mdi-delete
        </v-icon>
      </template>
    </DynamicTable>
  </v-container>
</template>

<script>
import { ref, onMounted } from 'vue'
import userService from '../services/userService'
import DynamicTable from '../components/ui/DynamicTable.vue'
import { useRouter } from 'vue-router'

export default {
  name: 'Main',
  components: { DynamicTable },
  setup() {
    const router = useRouter()
    const users = ref([])

    const formatDate = (timestamp) => {
      const date = new Date(timestamp * 1000)
      const pad = (num) => num.toString().padStart(2, '0')
      return `${pad(date.getMonth() + 1)}/${pad(date.getDate())}/${date.getFullYear()} ${pad(date.getHours())}:${pad(date.getMinutes())}:${pad(date.getSeconds())}`
    }
    const tableHeaders = ref([
      { field: 'username', label: 'Username', sortable: true },
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
      router.push({ name: 'UserPage' })
    }

    const openEditModal = (user) => {
      router.push({ name: 'UserPage', params: { id: user._id, user: user } })
    }

    const confirmDelete = async (user) => {
      if (confirm(`Are you sure you want to delete the user ${user.username}?`)) {
        try {
          await userService.deleteUser(user._id)
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
<style scoped>
.action-icon {
  /* Make the icon look clickable */
  cursor: pointer;
  /* Optional spacing between icons */
  margin-right: 8px;
  /* Keep icons vertically aligned with text */
  vertical-align: middle;
}
</style>