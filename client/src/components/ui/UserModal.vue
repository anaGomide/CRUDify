<template>
  <v-dialog v-model="dialog" persistent max-width="600px">
    <v-card>
      <v-card-title>
        {{ isEditMode ? 'Edit User' : 'Create User' }}
      </v-card-title>
      <v-card-text>
        <v-form ref="userForm" v-model="valid" lazy-validation>
          <v-text-field v-model="localUser.username" label="Username" :rules="[rules.required]" required></v-text-field>

          <v-text-field v-model="localUser.password" label="Password" type="password" :rules="[rules.required]"
            required></v-text-field>

          <v-select v-model="localUser.roles" :items="roleOptions" label="Roles" multiple :rules="[rules.required]"
            required></v-select>

          <v-select v-model="localUser.isActive" :items="activeOptions" label="Is Active?" :rules="[rules.required]"
            required></v-select>

          <v-select v-model="localUser.timezone" :items="timezoneOptions" label="Timezone" :rules="[rules.required]"
            required></v-select>

          <template v-if="isEditMode">
            <v-text-field
              v-model="localUser.created_ts"
              label="Created At"
              disabled
            ></v-text-field>

            <v-text-field
              v-model="localUser.updated_ts"
              label="Last Updated"
              disabled
            ></v-text-field>
          </template>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-btn color="primary" @click="handleSave" :disabled="!valid">
          Save
        </v-btn>
        <v-btn text @click="handleCancel">
          Cancel
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { ref, reactive, computed, watch } from 'vue'

export default {
  name: 'UserModal',
  props: {
    visible: {
      type: Boolean,
      default: false
    },
    userData: {
      type: Object,
      default: () => ({
        username: '',
        password: '',
        roles: [],
        isActive: '',
        timezone: '',
        created_ts: '',
        updated_ts: ''
      })
    },
    isEditMode: {
      type: Boolean,
      default: false
    }
  },
  emits: ['save', 'cancel', 'update:visible'],
  setup(props, { emit }) {
    const dialog = computed({
      get: () => props.visible,
      set: (value) => emit('update:visible', value)
    })

    const valid = ref(false)
    const userForm = ref(null)
    const localUser = reactive({ ...props.userData })
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
    const rules = {
      required: value => !!value || 'Required.'
    }

    watch(
      () => dialog.value,
      (newVal) => {
        if (newVal) {
          Object.assign(localUser, {
            username: '',
            password: '',
            roles: [],
            isActive: '',
            preferences: {
              timezone: ''
            },
            created_ts: '',
            updated_ts: '',
            ...props.userData
          })
        }
      }
    )

    const handleSave = () => {
      if (!userForm.value.validate()) return
      const payload = {
        username: localUser.username,
        password: localUser.password,
        roles: localUser.roles,
        active: localUser.isActive === 'Yes',
        preferences: {
          timezone: localUser.timezone
        }
      }
      emit('save', payload)
      dialog.value = false
    }

    const handleCancel = () => {
      emit('cancel')
      dialog.value = false
    }

    return {
      dialog,
      valid,
      userForm,
      localUser,
      roleOptions,
      activeOptions,
      timezoneOptions,
      rules,
      handleSave,
      handleCancel
    }
  }
}
</script>