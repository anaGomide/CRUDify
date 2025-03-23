// src/services/userService.js
import axios from 'axios'
import api from '../services/api'


const API_URL = 'http://localhost:5000'


const userService = {

  listUsers() {
    return axios.get(`${API_URL}/users/list`)
  },

  // listUsers() {
  //   return api.get('/users/list')
  // },
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
