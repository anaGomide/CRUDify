<template>
  <v-container>
    <v-card class="pa-4" outlined>
      <v-card-title>User Details</v-card-title>
      <v-card-text v-if="userLoaded">
        <table class="user-details-table">
          <tr>
            <td><strong>Username:</strong></td>
            <td>{{ user.username }}</td>
          </tr>
          <tr>
            <td><strong>Roles:</strong></td>
            <td>{{ Array.isArray(user.roles) ? user.roles.join(', ') : '' }}</td>
          </tr>
          <tr>
            <td><strong>Timezone:</strong></td>
            <td>{{ user.preferences?.timezone }}</td>
          </tr>
          <tr>
            <td><strong>Active:</strong></td>
            <td>{{ user.active ? 'Yes' : 'No' }}</td>
          </tr>
          <tr v-if="user.created_ts">
            <td><strong>Created At:</strong></td>
            <td>{{ formatDate(user.created_ts) }}</td>
          </tr>
          <tr v-if="user.updated_ts">
            <td><strong>Last Updated:</strong></td>
            <td>{{ formatDate(user.updated_ts) }}</td>
          </tr>
        </table>
      </v-card-text>
      <v-card-text v-else>
        Loading user data...
      </v-card-text>
      <v-card-actions>
        <v-btn text @click="goBack">Cancel</v-btn>
        <v-spacer></v-spacer>
        <v-btn color="primary" @click="openEditModal">Edit</v-btn>
        <v-btn color="error" @click="confirmDelete">Delete</v-btn>
      </v-card-actions>
    </v-card>

    <!-- Modal para edição -->
    <UserModal
      v-model:visible="showModal"
      :isEditMode="true"
      :userData="user"
      @save="handleSaveUser"
      @cancel="handleCancel"
    />
  </v-container>
</template>

<script>
import { reactive, ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import userService from '../services/userService'
import UserModal from '../components/ui/UserModal.vue'
import { formatDate } from "../helpers/dateHelper";


export default {
  name: 'UserPage',
  components: { UserModal },
  setup() {
    const router = useRouter()
    const route = useRoute()
    const user = reactive({
      username: '',
      password: '',
      roles: [],
      active: false,
      timezone: '',
      created_ts: '',
      updated_ts: ''
    })
    const userLoaded = ref(false)
    const showModal = ref(false)

    const loadUser = async () => {
      try {
        const response = await userService.viewUser(route.params.id)
        Object.assign(user, response.data)
        userLoaded.value = true
      } catch (error) {
        console.error('Error fetching user:', error)
        userLoaded.value = false
      }
    }

    const openEditModal = () => {
      showModal.value = true
    }

    const handleSaveUser = async (payload) => {
      try {
        await userService.updateUser(user._id, payload)
        console.log('User updated:', payload)
        // Atualiza os dados locais com os valores enviados
        Object.assign(user, {
          username: payload.username,
          password: payload.password,
          roles: payload.roles,
          active: payload.active,
          preferences: payload.preferences
        })
        showModal.value = false
      } catch (error) {
        console.error('Error updating user:', error)
      }
    }

    const handleCancel = () => {
      showModal.value = false
    }

    const confirmDelete = async () => {
      if (confirm(`Are you sure you want to delete the user ${user.username}?`)) {
        try {
          await userService.deleteUser(user._id)
          router.push({ name: 'Main' })
        } catch (error) {
          console.error('Error deleting user:', error)
        }
      }
    }

    const goBack = () => {
      router.back()
    }

    onMounted(() => {
      loadUser()
    })

    return {
      user,
      userLoaded,
      formatDate,
      openEditModal,
      confirmDelete,
      showModal,
      handleSaveUser,
      handleCancel,
      goBack
    }
  }
}
</script>

<style scoped>
.user-details-table {
  width: 100%;
  border-collapse: collapse;
}

.user-details-table td {
  padding: 8px;
  vertical-align: top;
}

.user-details-table tr:nth-child(odd) {
  background-color: #f9f9f9;
}

.user-details-table tr:nth-child(even) {
  background-color: #ffffff;
}
</style>
