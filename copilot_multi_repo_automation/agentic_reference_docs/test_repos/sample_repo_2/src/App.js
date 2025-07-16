import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import axios from 'axios';
import { useQuery, QueryClient, QueryClientProvider } from 'react-query';
import { ToastContainer, toast } from 'react-toastify';
import styled from 'styled-components';
import 'react-toastify/dist/ReactToastify.css';

// Styled Components
const AppContainer = styled.div`
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
`;

const Header = styled.header`
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  padding: 1rem 2rem;
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
`;

const Nav = styled.nav`
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
`;

const Logo = styled.h1`
  color: white;
  margin: 0;
  font-size: 1.8rem;
  font-weight: 600;
`;

const NavLinks = styled.div`
  display: flex;
  gap: 2rem;
  
  a {
    color: white;
    text-decoration: none;
    font-weight: 500;
    transition: opacity 0.3s ease;
    
    &:hover {
      opacity: 0.8;
    }
  }
`;

const MainContent = styled.main`
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
`;

const Card = styled.div`
  background: rgba(255, 255, 255, 0.95);
  border-radius: 12px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(10px);
`;

const Grid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
`;

const Button = styled.button`
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s ease;
  
  &:hover {
    transform: translateY(-2px);
  }
  
  &:disabled {
    opacity: 0.6;
    cursor: not-allowed;
    transform: none;
  }
`;

const LoadingSpinner = styled.div`
  border: 3px solid #f3f3f3;
  border-top: 3px solid #667eea;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
  margin: 2rem auto;
  
  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
`;

// API Configuration
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api/v1';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// API Functions
const fetchUsers = async () => {
  const response = await apiClient.get('/users');
  return response.data.users;
};

const fetchProducts = async () => {
  const response = await apiClient.get('/products');
  return response.data.products;
};

const createUser = async (userData) => {
  const response = await apiClient.post('/users', userData);
  return response.data.user;
};

const createProduct = async (productData) => {
  const response = await apiClient.post('/products', productData);
  return response.data.product;
};

// Components
const Dashboard = () => {
  const { data: users, isLoading: usersLoading, error: usersError } = useQuery('users', fetchUsers);
  const { data: products, isLoading: productsLoading, error: productsError } = useQuery('products', fetchProducts);

  if (usersLoading || productsLoading) {
    return (
      <Card>
        <h2>Loading Dashboard...</h2>
        <LoadingSpinner />
      </Card>
    );
  }

  if (usersError || productsError) {
    return (
      <Card>
        <h2>Error Loading Dashboard</h2>
        <p>Unable to fetch data from the API. Please try again later.</p>
      </Card>
    );
  }

  return (
    <div>
      <Card>
        <h2>📊 Dashboard Overview</h2>
        <Grid>
          <div>
            <h3>👥 Users</h3>
            <p>Total Users: <strong>{users?.length || 0}</strong></p>
            <p>Admins: <strong>{users?.filter(u => u.role === 'admin').length || 0}</strong></p>
          </div>
          <div>
            <h3>📦 Products</h3>
            <p>Total Products: <strong>{products?.length || 0}</strong></p>
            <p>Categories: <strong>{new Set(products?.map(p => p.category)).size || 0}</strong></p>
          </div>
        </Grid>
      </Card>
    </div>
  );
};

const UsersPage = () => {
  const { data: users, isLoading, error, refetch } = useQuery('users', fetchUsers);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({ name: '', email: '', role: 'user' });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await createUser(formData);
      toast.success('User created successfully!');
      setFormData({ name: '', email: '', role: 'user' });
      setShowForm(false);
      refetch();
    } catch (error) {
      toast.error('Failed to create user');
    }
  };

  if (isLoading) return <Card><LoadingSpinner /></Card>;
  if (error) return <Card><p>Error loading users</p></Card>;

  return (
    <div>
      <Card>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h2>👥 Users Management</h2>
          <Button onClick={() => setShowForm(!showForm)}>
            {showForm ? 'Cancel' : 'Add User'}
          </Button>
        </div>
        
        {showForm && (
          <form onSubmit={handleSubmit} style={{ marginTop: '2rem', padding: '1rem', background: '#f8f9fa', borderRadius: '8px' }}>
            <div style={{ marginBottom: '1rem' }}>
              <label>Name:</label>
              <input
                type="text"
                value={formData.name}
                onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                required
                style={{ width: '100%', padding: '0.5rem', marginTop: '0.25rem' }}
              />
            </div>
            <div style={{ marginBottom: '1rem' }}>
              <label>Email:</label>
              <input
                type="email"
                value={formData.email}
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                required
                style={{ width: '100%', padding: '0.5rem', marginTop: '0.25rem' }}
              />
            </div>
            <div style={{ marginBottom: '1rem' }}>
              <label>Role:</label>
              <select
                value={formData.role}
                onChange={(e) => setFormData({ ...formData, role: e.target.value })}
                style={{ width: '100%', padding: '0.5rem', marginTop: '0.25rem' }}
              >
                <option value="user">User</option>
                <option value="admin">Admin</option>
              </select>
            </div>
            <Button type="submit">Create User</Button>
          </form>
        )}
        
        <Grid>
          {users?.map(user => (
            <div key={user.id} style={{ padding: '1rem', background: '#f8f9fa', borderRadius: '8px' }}>
              <h4>{user.name}</h4>
              <p>📧 {user.email}</p>
              <p>🔑 {user.role}</p>
            </div>
          ))}
        </Grid>
      </Card>
    </div>
  );
};

const ProductsPage = () => {
  const { data: products, isLoading, error, refetch } = useQuery('products', fetchProducts);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({ name: '', price: '', category: '' });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await createProduct(formData);
      toast.success('Product created successfully!');
      setFormData({ name: '', price: '', category: '' });
      setShowForm(false);
      refetch();
    } catch (error) {
      toast.error('Failed to create product');
    }
  };

  if (isLoading) return <Card><LoadingSpinner /></Card>;
  if (error) return <Card><p>Error loading products</p></Card>;

  return (
    <div>
      <Card>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h2>📦 Products Management</h2>
          <Button onClick={() => setShowForm(!showForm)}>
            {showForm ? 'Cancel' : 'Add Product'}
          </Button>
        </div>
        
        {showForm && (
          <form onSubmit={handleSubmit} style={{ marginTop: '2rem', padding: '1rem', background: '#f8f9fa', borderRadius: '8px' }}>
            <div style={{ marginBottom: '1rem' }}>
              <label>Name:</label>
              <input
                type="text"
                value={formData.name}
                onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                required
                style={{ width: '100%', padding: '0.5rem', marginTop: '0.25rem' }}
              />
            </div>
            <div style={{ marginBottom: '1rem' }}>
              <label>Price:</label>
              <input
                type="number"
                step="0.01"
                value={formData.price}
                onChange={(e) => setFormData({ ...formData, price: e.target.value })}
                required
                style={{ width: '100%', padding: '0.5rem', marginTop: '0.25rem' }}
              />
            </div>
            <div style={{ marginBottom: '1rem' }}>
              <label>Category:</label>
              <input
                type="text"
                value={formData.category}
                onChange={(e) => setFormData({ ...formData, category: e.target.value })}
                required
                style={{ width: '100%', padding: '0.5rem', marginTop: '0.25rem' }}
              />
            </div>
            <Button type="submit">Create Product</Button>
          </form>
        )}
        
        <Grid>
          {products?.map(product => (
            <div key={product.id} style={{ padding: '1rem', background: '#f8f9fa', borderRadius: '8px' }}>
              <h4>{product.name}</h4>
              <p>💰 ${product.price}</p>
              <p>🏷️ {product.category}</p>
            </div>
          ))}
        </Grid>
      </Card>
    </div>
  );
};

// Main App Component
const App = () => {
  const queryClient = new QueryClient({
    defaultOptions: {
      queries: {
        retry: 2,
        staleTime: 5 * 60 * 1000, // 5 minutes
      },
    },
  });

  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <AppContainer>
          <Header>
            <Nav>
              <Logo>🚀 Sample Frontend App</Logo>
              <NavLinks>
                <Link to="/">Dashboard</Link>
                <Link to="/users">Users</Link>
                <Link to="/products">Products</Link>
              </NavLinks>
            </Nav>
          </Header>
          
          <MainContent>
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/users" element={<UsersPage />} />
              <Route path="/products" element={<ProductsPage />} />
            </Routes>
          </MainContent>
          
          <ToastContainer
            position="top-right"
            autoClose={3000}
            hideProgressBar={false}
            newestOnTop={false}
            closeOnClick
            rtl={false}
            pauseOnFocusLoss
            draggable
            pauseOnHover
          />
        </AppContainer>
      </Router>
    </QueryClientProvider>
  );
};

export default App;