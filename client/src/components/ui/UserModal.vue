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

          <!-- Updated v-select to handle active (boolean) -->
          <v-select v-model="localUser.active" :items="activeOptions" label="Active?" item-title="text"
            item-value="value" :rules="[rules.required]" required></v-select>

          <v-select v-model="localUser.timezone" :items="timezoneOptions" label="Timezone" :rules="[rules.required]"
            required></v-select>

          <template v-if="isEditMode">
            <!-- Use computed properties to display formatted dates -->
            <v-text-field v-model="createdDate" label="Created At" disabled></v-text-field>
            <v-text-field v-model="updatedDate" label="Last Updated" disabled></v-text-field>
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
import { formatDate } from "../../helpers/dateHelper";

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
        active: false,
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
    const activeOptions = [
      { text: 'Yes', value: true },
      { text: 'No', value: false }
    ]
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
      required: value => value !== null && value !== undefined && value !== '' || 'Required.'
    }

    // Create computed properties for formatted dates.
    const createdDate = computed(() => {
      return localUser.created_ts ? formatDate(localUser.created_ts) : ''
    })

    const updatedDate = computed(() => {
      return localUser.updated_ts ? formatDate(localUser.updated_ts) : ''
    })

    watch(
      () => dialog.value,
      (newVal) => {
        if (newVal) {
          Object.assign(localUser, {
            username: '',
            password: '',
            roles: [],
            active: false,
            timezone: '',
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
        active: localUser.active,
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
      handleCancel,
      createdDate,
      updatedDate
    }
  }
}
</script>
