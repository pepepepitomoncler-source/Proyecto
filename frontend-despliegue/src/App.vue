<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <!-- Top app bar de M3: fondo surface-container -->
  <header class="app-header">
    <RouterLink to="/" class="brand" aria-label="Check&Fit, ir a Inicio">
      Check<span class="brand__amp">&amp;</span>Fit
    </RouterLink>

    <nav aria-label="Principal">
      <RouterLink to="/">Inicio</RouterLink>
      <RouterLink to="/hello">Hello</RouterLink>
    </nav>
  </header>

  <main class="app-main">
    <RouterView />
  </main>
</template>

<style scoped>
.app-header {
  position: sticky;
  top: 0;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 64px;
  padding: 0 var(--space-m);
  background: var(--color-surface-container);
}

.brand {
  font-size: var(--font-size-result);
  font-weight: var(--font-weight-medium);
  color: var(--color-on-surface);
  text-decoration: none;
  border-radius: var(--radius-xs);
}

.brand__amp {
  color: var(--color-primary);
}

nav {
  display: flex;
  gap: var(--space-s);
}

/* Destinos de navegación: zona táctil de 48 px e indicador en píldora */
nav a {
  display: inline-flex;
  align-items: center;
  min-height: 48px;
  padding: 0 var(--space-m);
  border-radius: var(--radius-full);
  color: var(--color-on-surface-variant);
  font-size: var(--font-size-label);
  font-weight: var(--font-weight-medium);
  text-decoration: none;
}

nav a:hover {
  background: color-mix(in srgb, var(--color-on-surface) var(--state-hover), transparent);
}

nav a.router-link-exact-active {
  background: var(--color-primary-container);
  color: var(--color-on-primary-container);
}

.app-main {
  max-width: 640px;
  margin: 0 auto;
  padding: var(--space-l) var(--space-m) var(--space-xl);
}

@media (min-width: 600px) {
  .app-main {
    padding-inline: var(--space-l);
  }
}
</style>
