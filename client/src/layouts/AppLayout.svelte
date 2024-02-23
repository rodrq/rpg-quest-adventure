<script>
    import { Router, Route } from 'svelte-routing';
    import Navbar from "../components/Navbar.svelte";
    import Footer from "../components/Footer.svelte";
    import Home from '../pages/Home.svelte';
    import Ranking from '../pages/Ranking.svelte';
    import About from '../pages/About.svelte';
    import Register from '../pages/Register.svelte';
  </script>
  
  <Navbar/>
    <Router>
      <Route path="/" component={Home} />
      <Route path="/about" component={About} />
      <Route path="/ranking" component={Ranking} />
      <Route path="/register" component={Register} />
    </Router>
  <Footer/>
  