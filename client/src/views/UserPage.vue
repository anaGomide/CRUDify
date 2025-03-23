<template>
  <v-container>
    <v-card class="pa-4" max-width="600" outlined>
      <v-card-title>
        {{ isEditMode ? 'Edit User' : 'Create User' }}
      </v-card-title>
      <v-card-text>
        <v-form ref="userForm" v-model="valid" lazy-validation>
          <v-text-field
            v-model="user.name"
            label="Name"
            :rules="[rules.required]"
            required
          ></v-text-field>

          <v-select
            v-model="user.role"
            :items="roleOptions"
            label="Role"
            :rules="[rules.required]"
            required
          ></v-select>

          <v-text-field
            v-model="user.createdAt"
            label="Created At"
            disabled
          ></v-text-field>

          <v-text-field
            v-model="user.updatedAt"
            label="Last Updated"
            disabled
          ></v-text-field>

          <v-select
            v-model="user.isActive"
            :items="activeOptions"
            label="Is Active?"
            :rules="[rules.required]"
            required
          ></v-select>

          <v-select
            v-model="user.timezone"
            :items="timezoneOptions"
            label="Timezone"
            :rules="[rules.required]"
            required
          ></v-select>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-btn color="primary" @click="saveUser" :disabled="!valid">
          Save
        </v-btn>
        <v-btn text @click="cancel">
          Cancel
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import { ref, reactive, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import userService from '../services/userService'

export default {
  name: 'UserPage',
  setup() {
    const router = useRouter()
    const route = useRoute()

    // Modo de edição: se houver um ID nos parâmetros, estamos editando
    const isEditMode = computed(() => !!route.params.id)

    // Objeto usuário para criação/edição
    const user = reactive({
      name: '',
      role: '',
      createdAt: '',
      updatedAt: '',
      isActive: '',
      timezone: ''
    })

    // Opções para os selects
    const roleOptions = ['Administrator', 'Manager', 'Test', 'No Role']
    const activeOptions = ['Yes', 'No']
    const timezoneOptions = [
      'UTC',
      'America/New_York',
      'America/Los_Angeles',
      'Europe/London',
      'Europe/Paris',
      'Asia/Tokyo',
      'Asia/Hong_Kong'
    ]

    // Validação básica
    const rules = {
      required: value => !!value || 'Required.'
    }

    const valid = ref(false)
    const userForm = ref(null)

    onMounted(() => {
      // Se estiver no modo de edição, preenche o formulário com os dados existentes
      // Aqui, assumimos que os dados do usuário foram passados via route.params.user.
      // Você pode também fazer uma chamada à API usando route.params.id, se necessário.
      if (isEditMode.value && route.params.user) {
        const existingUser = route.params.user
        user.name = existingUser.name || ''
        user.role = existingUser.role || ''
        user.createdAt = existingUser.createdAt || ''  // Considere mapear para existingUser.created_ts, se aplicável
        user.updatedAt = existingUser.updatedAt || ''  // Considere mapear para existingUser.updated_ts, se aplicável
        user.isActive = existingUser.isActive ? 'Yes' : 'No'
        user.timezone = existingUser.timezone || ''
      }
    })

    const saveUser = async () => {
      if (!userForm.value.validate()) return

      // Converter isActive de 'Yes'/'No' para booleano
      const payload = {
        ...user,
        isActive: user.isActive === 'Yes'
      }

      try {
        if (isEditMode.value) {
          await userService.updateUser(route.params.id, payload)
          console.log('User updated:', payload)
        } else {
          await userService.createUser(payload)
          console.log('User created:', payload)
        }
        router.push({ name: 'Main' })
      } catch (error) {
        console.error(isEditMode.value ? 'Error updating user:' : 'Error creating user:', error)
      }
    }

    const cancel = () => {
      router.push({ name: 'Main' })
    }

    return {
      user,
      isEditMode,
      roleOptions,
      activeOptions,
      timezoneOptions,
      rules,
      valid,
      userForm,
      saveUser,
      cancel
    }
  }
}
</script>

<style scoped>
/* Adicione estilos específicos, se necessário */
</style>
