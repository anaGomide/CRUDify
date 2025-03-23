// src/services/userService.js
import api from '@/services/api'

const userService = {
  listUsers() {
    return api.get('/users/list')
  },
  viewUser(id) {
    return api.get(`/users/view/${id}`)
  },
  createUser(userData) {
    return api.post('/users/create', userData)
  },
  updateUser(id, userData) {
    return api.put(`/user/update/${id}`, userData)
  },
  deleteUser(id) {
    return api.delete(`/users/delete/${id}`)
  }
}

export default userService
