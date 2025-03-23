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
          <slot name="actions" :item="item">
            <v-icon
              color="green"
              class="action-icon"
            >
              mdi-pencil
            </v-icon>
            <v-icon
              color="red"
              class="action-icon"
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

.header-cell {
  background-color: #9c27b0;
  color: white;
  transition: background-color 0.3s;
  padding: 8px;
}

.header-cell:hover {
  background-color: #ab47bc;
}

tbody tr:nth-child(odd) {
  background-color: #ffffff;
}

tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}

tbody tr:hover {
  background-color: #e1bee7;
}

.action-icon {
  margin-right: 24px;
  cursor: pointer;   
  vertical-align: middle;
}
</style>
