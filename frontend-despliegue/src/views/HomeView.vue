<template>
  <section class="home">
    <h1>Bienvenido a Check&amp;Fit</h1>
    <p>
      Tu entrenador y tú, en la misma página. Esta primera pantalla consume el endpoint
      <code>/api/hello</code> de nuestro backend Laravel.
    </p>
    <RouterLink to="/hello" class="btn-filled">Ir al saludo</RouterLink>
  </section>
</template>

<style scoped>
/* Tarjeta filled de M3 */
.home {
  padding: var(--space-l);
  border-radius: var(--radius-m);
  background: var(--color-surface-container);
}

code {
  padding: 0 var(--space-xs);
  border-radius: var(--radius-xs);
  background: var(--color-surface);
}
</style>
