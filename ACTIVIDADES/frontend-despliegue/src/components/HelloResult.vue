<script setup>
// Zona de resultado con los cuatro estados de DESIGN.md:
// vacío, cargando, resultado correcto y error.
defineProps({
  message: { type: String, default: '' },
  error: { type: String, default: '' },
  loading: { type: Boolean, default: false },
})
</script>

<template>
  <div class="result-zone" aria-live="polite">
    <!-- Error -->
    <div v-if="error" class="result result--error" role="alert">
      <svg class="result__icon" width="24" height="24" viewBox="0 0 24 24" aria-hidden="true">
        <circle cx="12" cy="12" r="10" fill="currentColor" />
        <path d="M12 7v6M12 16.5v.5" stroke="var(--color-error-container)" stroke-width="2.2" stroke-linecap="round" />
      </svg>
      <div>
        <strong class="result__title">No se ha podido contactar con el backend</strong>
        <span>{{ error }}</span>
      </div>
    </div>

    <!-- Cargando -->
    <div v-else-if="loading" class="result">
      <span class="spinner" role="progressbar" aria-label="Cargando"></span>
      <span>Conectando…</span>
    </div>

    <!-- Resultado correcto -->
    <p v-else-if="message" class="result result--success">{{ message }}</p>

    <!-- Vacío -->
    <p v-else class="result result--empty">Aquí aparecerá el saludo.</p>
  </div>
</template>

<style scoped>
.result-zone {
  margin-top: var(--space-l);
}

/* Tarjeta filled de M3: radio medium (12 px), padding 16 px */
.result {
  display: flex;
  align-items: center;
  gap: var(--space-m);
  min-height: 88px;
  margin: 0;
  padding: var(--space-m);
  border-radius: var(--radius-m);
  background: var(--color-surface-container);
  color: var(--color-on-surface-variant);
}

.result--success {
  background: var(--color-primary-container);
  color: var(--color-on-primary-container);
  font-size: var(--font-size-result);
  line-height: 28px;
}

.result--error {
  background: var(--color-error-container);
  color: var(--color-on-error-container);
}

.result__title {
  display: block;
  font-weight: var(--font-weight-medium);
}

.result__icon {
  flex: none;
}

/* Indicador circular de progreso (indeterminado) */
.spinner {
  flex: none;
  width: 32px;
  height: 32px;
  border: 4px solid var(--color-primary-container);
  border-top-color: var(--color-primary);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .spinner {
    animation-duration: 3s;
  }
}
</style>
