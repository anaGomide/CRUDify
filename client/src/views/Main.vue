<template>
  <v-container>
    <v-btn class="mb-4" color="primary" @click="openCreateModal">Criar Usuário</v-btn>
    <!-- <pre>{{ users }}</pre> -->

    <v-table>
    <thead>
      <tr>
        <th class="text-left">
          Username 
        </th>
        <th class="text-left">
          Roles 
        </th>
        <th class="text-left">
          Timezone 
        </th>
        <th class="text-left">
          Is Active?
        </th>
        <th class="text-left">
          Last Updated At
        </th>
        <th class="text-left">
          Created At
        </th>
        <th class="text-left">
          Actions
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="user in users"
        :key="user._id"
      >
        <td>{{ user.username }}</td>
        <td>{{ user.roles }}</td>
        <td>{{ user.preferences.timezone }}</td>
        <td>{{ user.active }}</td>
        <td> last update </td>
        <td>{{ user.created_ts }}</td>
        <td> actions here</td>

      </tr>
    </tbody>
  </v-table>

    <!-- <v-data-table :items="users" :headers="headers" class="elevation-1">
      <template v-slot:item.username="{ item }">
        <router-link :to="{ name: 'UserPage', params: { id: item._id.$oid } }">
          {{ item.username }}
        </router-link>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-btn small color="secondary" @click="openEditModal(item)">Editar</v-btn>
        <v-btn small color="error" @click="confirmDelete(item)">Excluir</v-btn>
      </template>
      <template v-slot:item.created_ts="{ item }">
        {{ formatDate(item.created_ts) }}
      </template>
    </v-data-table> -->

    <!-- Modal para Criação/Edição -->
    <!-- <UserFormDialog
      v-if="dialogVisible"
      :user="selectedUser"
      @close="dialogVisible = false"
      @saved="handleSaved"
    /> -->
  </v-container>
</template>

<script>
import { ref, onMounted } from 'vue'
import userService from '../services/userService'
//import UserFormDialog from '@/components/UserFormDialog.vue'

export default {
  name: 'Main',
  //components: { UserFormDialog },
  setup() {
    const users = ref([])
    const dialogVisible = ref(false)
    const selectedUser = ref(null)

    // Definição dos cabeçalhos para o v-data-table
    const headers = [
      { text: 'Nome de Usuário', value: 'username' },
      { text: 'Funções', value: 'roles' },
      { text: 'Fuso Horário', value: 'preferences.timezone' },
      { text: 'Está Ativo?', value: 'active' },
      { text: 'Criado Em', value: 'created_ts' },
      { text: 'Ações', value: '', sortable: false }
    ]

    const fetchUsers = async () => {
      try {
        const response = await userService.listUsers()
        console.log("Dados recebidos:", response.data)
        // Se a resposta for um array, use direto; se for um objeto, extraia a propriedade correta
        users.value = Array.isArray(response.data)
          ? response.data
          : response.data.users || []
      } catch (error) {
        console.error('Erro ao buscar usuários:', error)
      }
    }

    const openCreateModal = () => {
      selectedUser.value = null
      dialogVisible.value = true
    }

    const openEditModal = (user) => {
      selectedUser.value = user
      dialogVisible.value = true
    }

    const confirmDelete = async (user) => {
      if (confirm(`Tem certeza que deseja excluir o usuário ${user.username}?`)) {
        try {
          await userService.deleteUser(user._id.$oid)
          fetchUsers()
        } catch (error) {
          console.error('Erro ao excluir o usuário:', error)
        }
      }
    }

    const handleSaved = () => {
      dialogVisible.value = false
      fetchUsers()
    }

    const formatDate = (timestamp) => {
      const date = new Date(timestamp * 1000)
      return date.toLocaleString()
    }

    onMounted(fetchUsers)

    return {
      users,
      headers,
      dialogVisible,
      selectedUser,
      fetchUsers,
      openCreateModal,
      openEditModal,
      confirmDelete,
      formatDate,
      handleSaved
    }
  }
}
</script>
