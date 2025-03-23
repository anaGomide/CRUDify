<template>
  <v-container>
    <h1>Detalhes do Usuário</h1>
    <div v-if="user">
      <p><strong>Nome de Usuário:</strong> {{ user.username }}</p>
      <p><strong>Funções:</strong> {{ user.roles.join(', ') }}</p>
      <p><strong>Fuso Horário:</strong> {{ user.preferences.timezone }}</p>
      <p><strong>Está Ativo:</strong> {{ user.active ? 'Sim' : 'Não' }}</p>
      <p><strong>Criado Em:</strong> {{ formatDate(user.created_ts) }}</p>
      <p><strong>Última Atualização Em:</strong> {{ user.updated_ts ? formatDate(user.updated_ts) : '-' }}</p>
      <v-btn color="secondary" @click="openEditModal">Editar</v-btn>
      <v-btn color="error" @click="confirmDelete">Excluir</v-btn>
    </div>
  </v-container>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import userService from '../services/userService'

export default {
  name: 'UserPage',
  setup() {
    const route = useRoute()
    const router = useRouter()
    const user = ref(null)

    const fetchUser = async () => {
      try {
        const response = await userService.viewUser(route.params.id)
        user.value = response.data
      } catch (error) {
        console.error('Erro ao buscar usuário:', error)
      }
    }

    const openEditModal = () => {
      // Aqui você pode abrir um modal similar ao do UserList
      // ou redirecionar para uma rota de edição, se preferir.
    }

    const confirmDelete = async () => {
      if (confirm(`Tem certeza que deseja excluir o usuário ${user.value.username}?`)) {
        try {
          await userService.deleteUser(user.value._id.$oid)
          router.push({ name: 'UserList' })
        } catch (error) {
          console.error('Erro ao excluir o usuário:', error)
        }
      }
    }

    const formatDate = (timestamp) => {
      const date = new Date(timestamp * 1000)
      return date.toLocaleString()
    }

    onMounted(fetchUser)

    return { user, openEditModal, confirmDelete, formatDate }
  }
}
</script>
