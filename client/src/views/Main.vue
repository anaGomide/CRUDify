<template>
   <v-container class="main-page-container">
    <div class="main-page-container__header">
      <h1 class="main-page-container__tittle">List Users</h1>
      <v-btn
        class="main-page-container__insert-button mb-4"
        color="#684b6e"
        @click="openCreateModal"
      >
        Insert user
      </v-btn>
    </div>

    <DynamicTable :items="users" :headers="tableHeaders">
      <template #username="{ item }">
        <span class="clickable" @click="openDetails(item)">{{ item.username }}</span>
      </template>
      <template #actions="{ item }">
        <v-icon color="green" class="action-icon" @click="openEditModal(item)">
          mdi-pencil-outline
        </v-icon>

        <v-icon color="red" class="action-icon" @click="confirmDelete(item)">
          mdi-trash-can-outline
        </v-icon>
      </template>
    </DynamicTable>
    <UserModal v-model:visible="showModal" :isEditMode="modalIsEditMode" :userData="selectedUser" @save="handleSaveUser"
      @cancel="handleCancel" />
  </v-container>
</template>

<script>
import { ref, onMounted } from 'vue'
import userService from '../services/userService'
import DynamicTable from '../components/ui/DynamicTable.vue'
import { useRouter } from 'vue-router'
import UserModal from '../components/ui/UserModal.vue'
import { formatDate } from "../helpers/dateHelper";

export default {
  name: 'Main',
  components: { DynamicTable, UserModal },
  setup() {
    const router = useRouter()
    const users = ref([])
    const showModal = ref(false)
    const modalIsEditMode = ref(false)
    const selectedUser = ref({
      username: '',
      password: '',
      roles: [],
      isActive: '',
      timezone: '',
      created_ts: '',
      updated_ts: ''
    })

    const tableHeaders = ref([
      { field: 'username', label: 'Username', sortable: true },
      {
        field: 'roles',
        label: 'Roles',
        render: (item) => Array.isArray(item.roles) ? item.roles.join(', ') : item.roles
      },
      {
        field: 'preferences.timezone',
        label: 'Timezone',
        render: (item) => item.preferences && item.preferences.timezone ? item.preferences.timezone : ''
      },
      {
        field: 'active',
        label: 'Is Active?',
        render: (item) => item.active ? 'Yes' : 'No'
      },
      {
        field: 'updated_ts',
        label: 'Last Updated At',
        render: (item) => item.updated_ts ? formatDate(item.updated_ts) : ''
      },
      {
        field: 'created_ts',
        label: 'Created At',
        render: (item) => item.created_ts ? formatDate(item.created_ts) : ''
      }
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
      console.log('Creating new user')
      modalIsEditMode.value = false
      selectedUser.value = {
        username: '',
        password: '',
        roles: [],
        isActive: '',
        timezone: '',
        created_ts: '',
        updated_ts: ''
      }
      showModal.value = true
    }

    const openEditModal = (user) => {
      modalIsEditMode.value = true
      selectedUser.value = {
        ...user,
        timezone: user.preferences?.timezone || ''
      }
      selectedUser.value.isActive = user.active ? 'Yes' : 'No'
      showModal.value = true
    }

    const openDetails = (user) => {
      console.log('Viewing user:', user)
      router.push({ name: 'UserPage', params: { id: user._id } })
    }


    const handleSaveUser = async (payload) => {
      try {
        if (modalIsEditMode.value) {
          await userService.updateUser(selectedUser.value._id, payload)
          console.log('User updated:', payload)
        } else {
          await userService.createUser(payload)
          console.log('User created:', payload)
        }
        await fetchUsers()
      } catch (error) {
        console.error(modalIsEditMode.value ? 'Error updating user:' : 'Error creating user:', error)
      }
    }

    const handleCancel = () => {
      showModal.value = false
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
      openDetails,
      confirmDelete,
      showModal,
      modalIsEditMode,
      selectedUser,
      handleSaveUser,
      handleCancel
    }
  }
}
</script>
<style lang="scss" scoped>
.action-icon {
  cursor: pointer;
  margin-right: 8px;
  vertical-align: middle;
}
.clickable {
  color: blue;
  text-decoration: underline;
  cursor: pointer;
}
.main-page-container {
  &__header {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin: 12px;
  }
}
</style>