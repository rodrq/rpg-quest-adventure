import "./app.pcss";
import AppLayout from '/src/layouts/AppLayout.svelte';


const app = new AppLayout({
  target: document.getElementById("app"),
});

export default app;
