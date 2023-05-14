<script lang="ts">
  import { colors } from '../constant'
  export let move: string
  export let back: boolean
</script>

<div class="mx-auto my-3 w-40 h-40 relative flex justify-center items-center">
  <table>
    {#each {length: 3} as _}
      <tr>
        {#each {length: 3} as __}
          <td class="w-8 h-8 border border-gray-500" />
        {/each}
      </tr>
    {/each}
  </table>
  <div class={`absolute top-2 left-[4.5rem] w-4 h-4 bg-${colors[0]} rounded-full`} />
  <div class={`absolute top-[4.5rem] right-2 w-4 h-4 bg-${back ? colors[4] : colors[1]} rounded-full`} />
  <div class={`absolute top-[4.5rem] left-[4.5rem] w-4 h-4 bg-${back ? colors[5] : colors[2]} rounded-full`} />
  <div class={`absolute bottom-2 left-[4.5rem] w-4 h-4 bg-${colors[3]} rounded-full`} />
  <div class={`absolute top-[4.5rem] left-2 w-4 h-4 bg-${back ? colors[1] : colors[4]} rounded-full`} />
  {#if move == 'U'}
    <div class="arrow scale-x-[-1]" />
  {:else if move == 'U\''}
    <div class="arrow" />
  {:else if move == 'U2'}
    <div class="arrow-2 scale-x-[-1]" />
  {:else if move == 'R'}
    {#if back}
      <div class="arrow scale-x-[-1] -rotate-90" />
    {:else}
      <div class="arrow scale-x-[-1] rotate-90" />
    {/if}
  {:else if move == 'R\''}
    {#if back}
      <div class="arrow -rotate-90" />
    {:else}
      <div class="arrow rotate-90" />
    {/if}
  {:else if move == 'R2'}
    {#if back}
      <div class="arrow-2 scale-x-[-1] -rotate-90" />
    {:else}
      <div class="arrow-2 scale-x-[-1] rotate-90" />
    {/if}
  {:else if move == 'F'}
    <div class="arrow-f" />
  {:else if move == 'F\''}
    <div class="arrow-f scale-x-[-1]" />
  {:else if move == 'F2'}
    <div class="arrow-f2" />
  {:else if move == 'D'}
    <div class="arrow scale-x-[-1] rotate-180" />
  {:else if move == 'D\''}
    <div class="arrow rotate-180" />
  {:else if move == 'D2'}
    <div class="arrow-2 scale-x-[-1] rotate-180" />
  {:else if move == 'L'}
    {#if back}
      <div class="arrow scale-x-[-1] rotate-90" />
    {:else}
      <div class="arrow scale-x-[-1] -rotate-90" />
    {/if}
  {:else if move == 'L\''}
    {#if back}
      <div class="arrow rotate-90" />
    {:else}
      <div class="arrow -rotate-90" />
    {/if}
  {:else if move == 'L2'}
    {#if back}
      <div class="arrow-2 scale-x-[-1] rotate-90" />
    {:else}
      <div class="arrow-2 scale-x-[-1] -rotate-90" />
    {/if}
  {:else if move == 'B'}
    <div class="arrow-f" />
  {:else if move == 'B\''}
    <div class="arrow-f scale-x-[-1]" />
  {:else if move == 'B2'}
    <div class="arrow-f2" />
  {/if}
</div>

<style>
  .arrow {
    @apply absolute w-24 h-24 bg-primary;
    clip-path: polygon(
      calc(100% / 6) calc(100% / 8),
      calc(100% * 5 / 8) calc(100% / 8),
      calc(100% * 5 / 8) calc(100% / 24),
      calc(100% * 5 / 6) calc(100% / 6),
      calc(100% * 5 / 8) calc(100% * 7 / 24),
      calc(100% * 5 / 8) calc(100% * 5 / 24),
      calc(100% / 6) calc(100% * 5 / 24),
      calc(100% / 6) calc(100% / 8)
      );
  }
  .arrow-2 {
    @apply absolute w-24 h-24 bg-accent;
    clip-path: polygon(
      calc(100% / 6) calc(100% / 8),
      calc(100% * 7 / 24) calc(100% / 8),
      calc(100% * 7 / 24) calc(100% / 24),
      50% calc(100% / 6),
      50% calc(100% / 8),
      calc(100% * 5 / 8) calc(100% / 8),
      calc(100% * 5 / 8) calc(100% / 24),
      calc(100% * 5 / 6) calc(100% / 6),
      calc(100% * 5 / 8) calc(100% * 7 / 24),
      calc(100% * 5 / 8) calc(100% * 5 / 24),
      50% calc(100% * 5 / 24),
      50% calc(100% / 6),
      calc(100% * 7 / 24) calc(100% * 7 / 24),
      calc(100% * 7 / 24) calc(100% * 5 / 24),
      calc(100% / 6) calc(100% * 5 / 24),
      calc(100% / 6) calc(100% / 8)
      );
  }
  .arrow-f {
    @apply absolute w-24 h-24 bg-primary;
    clip-path: polygon(
      calc(100% / 8) 50%,
      calc(100% / 8) calc(100% / 8),
      calc(100% * 7 / 24) calc(100% / 8),
      calc(100% * 7 / 24) calc(100% / 24),
      50% calc(100% / 6),
      calc(100% * 7 / 24) calc(100% * 7 / 24),
      calc(100% * 7 / 24) calc(100% * 5 / 24),
      calc(100% * 5 / 24) calc(100% * 5 / 24),
      calc(100% * 5 / 24) 50%,
      calc(100% * 7 / 8) 50%,
      calc(100% * 7 / 8) calc(100% * 7 / 8),
      calc(100% * 17 / 24) calc(100% * 7 / 8),
      calc(100% * 17 / 24) calc(100% * 23 / 24),
      50% calc(100% * 5 / 6),
      calc(100% * 17 / 24) calc(100% * 17 / 24),
      calc(100% * 17 / 24) calc(100% * 19 / 24),
      calc(100% * 19 / 24) calc(100% * 19 / 24),
      calc(100% * 19 / 24) 50%,
      calc(100% / 8) 50%
      );
  }
  .arrow-f2 {
    @apply absolute w-24 h-24 bg-accent;
    clip-path: polygon(
      calc(100% / 8) calc(100% * 5 / 12),
      calc(100% / 8) calc(100% / 8),
      calc(100% * 7 / 8) calc(100% / 8),
      calc(100% * 7 / 8) calc(100% * 7 / 24),
      calc(100% * 23 / 24) calc(100% * 7 / 24),
      calc(100% * 5 / 6) 50%,
      calc(100% * 19 / 24) calc(100% * 7 / 12),
      calc(100% * 7 / 8) calc(100% * 7 / 12),
      calc(100% * 7 / 8) calc(100% * 7 / 8),
      calc(100% / 8) calc(100% * 7 / 8),
      calc(100% / 8) calc(100% * 17 / 24),
      calc(100% / 24) calc(100% * 17 / 24),
      calc(100% / 6) 50%,
      calc(100% * 7 / 24) calc(100% * 17 / 24),
      calc(100% * 5 / 24) calc(100% * 17 / 24),
      calc(100% * 5 / 24) calc(100% * 19 / 24),
      calc(100% * 19 / 24) calc(100% * 19 / 24),
      calc(100% * 19 / 24) calc(100% * 7 / 12),
      calc(100% * 5 / 6) 50%,
      calc(100% * 17 / 24) calc(100% * 7 / 24),
      calc(100% * 19 / 24) calc(100% * 7 / 24),
      calc(100% * 19 / 24) calc(100% * 5 / 24),
      calc(100% * 5 / 24) calc(100% * 5 / 24),
      calc(100% * 5 / 24) calc(100% * 5 / 12),
      calc(100% / 8) calc(100% * 5 / 12)
      );
  }
</style>
