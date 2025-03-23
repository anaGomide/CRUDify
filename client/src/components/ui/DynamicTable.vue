<template>
  <v-table class="rounded-table">
    <thead>
      <tr>
        <th
          v-for="header in headers"
          :key="header.field"
          class="text-left header-cell"
        >
          {{ header.label }}
        </th>
        <th v-if="$slots.actions" class="text-left header-cell">Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(item, index) in items" :key="item._id || index">
        <td v-for="header in headers" :key="header.field">
          <slot :name="header.field" :item="item">
            {{ renderCell(item, header) }}
          </slot>
        </td>
        <td v-if="$slots.actions">
          <!-- Use plain icons without buttons -->
          <slot name="actions" :item="item">
            <v-icon
              color="green"
              class="action-icon"
              @click="editItem(item)"
            >
              mdi-pencil
            </v-icon>
            <v-icon
              color="red"
              class="action-icon"
              @click="deleteItem(item)"
            >
              mdi-delete
            </v-icon>
          </slot>
        </td>
      </tr>
    </tbody>
  </v-table>
</template>

<script>
export default {
  name: 'DynamicTable',
  props: {
    items: {
      type: Array,
      default: () => []
    },
    headers: {
      type: Array,
      default: () => []
    }
  },
  methods: {
    renderCell(item, header) {
      if (typeof header.render === 'function') {
        return header.render(item)
      } else {
        const keys = header.field.split('.')
        return keys.reduce((acc, key) => (acc ? acc[key] : ''), item)
      }
    },
    editItem(item) {
      // Your edit logic here
      console.log('Edit:', item)
    },
    deleteItem(item) {
      // Your delete logic here
      console.log('Delete:', item)
    }
  }
}
</script>

<style scoped>
.rounded-table {
  border-collapse: separate;
  border-spacing: 0;
  border-radius: 10px;
  overflow: hidden;
}

/* Header styling: purple background, white text, with lighter purple on hover */
.header-cell {
  background-color: #9c27b0;
  color: white;
  transition: background-color 0.3s;
  padding: 8px;
}

.header-cell:hover {
  background-color: #ab47bc;
}

/* Alternate row colors: odd rows white, even rows very light gray */
tbody tr:nth-child(odd) {
  background-color: #ffffff;
}

tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}

/* Row hover effect: light purple background */
tbody tr:hover {
  background-color: #e1bee7;
}

/* Optional: style the icons to show a pointer on hover */
.action-icon {
  margin-right: 24px;       /* spacing between icons */
  cursor: pointer;         /* show pointer cursor on hover */
  vertical-align: middle;  /* keep icons vertically aligned */
}
</style>
