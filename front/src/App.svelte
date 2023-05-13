<script lang="ts">
  import axios from 'axios'

  let cubestr: string = ''
  let result: string = ''

  const solve = () => {
    axios.get('/api', { params: { cubestr } })
      .then(res => {
        result = res.data.solution
      })
  }
</script>

<div class="p-6">
  <input type="text" placeholder="Type here" bind:value={cubestr} class="input input-bordered w-full max-w-xs block mx-auto" />
  <button on:click={solve} class="btn btn-primary w-full max-w-xs block mx-auto mt-3">Solve</button>
  <div class="mt-3 text-center">
    {result}
  </div>
</div>
