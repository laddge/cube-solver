<script lang="ts">
  import axios from 'axios'

  const colors = ['blue-500', 'red-500', 'white', 'green-500', 'orange-500', 'yellow-500']
  const cube = {
    U5: 0,
    R5: 1,
    F5: 2,
    D5: 3,
    L5: 4,
    B5: 5,
  }

  let radioValue: number = 0
  let cubestr: string = 'URFDLB'
  let result: string = ''

  $: {
    if (Object.values(cube).filter(val => val == radioValue).length > 8) {
      let ok: boolean = false
      for (let i: number = 1; i < 6; i++) {
        if (Object.values(cube).filter(val => val == (radioValue + i) % 6) <= 8) {
          radioValue = (radioValue + i) % 6
          ok = true
          break
        }
      }
      if (!ok) radioValue = -1
    }
  }

  const write = (id: string) => {
    if (id.slice(-1) == '5') retdrn
    cube[id] = radioValue
    cubestr = ''
    const sfcs = ['U', 'R', 'F', 'D', 'L', 'B']
    for (const sfc of sfcs) {
      for (let i: number = 1; i <= 9; i++) {
        if (cube[`${sfc}${i}`] != undefined) {
          cubestr += sfcs[cube[`${sfc}${i}`]]
        }
      }
    }
  }

  const solve = () => {
    axios.get('/api', { params: { cubestr } })
      .then(res => {
        result = res.data.solution
      })
  }
</script>

<div class="hidden bg-gray-500 bg-blue-500 bg-red-500 bg-white bg-green-500 bg-orange-500 bg-yellow-500 checked:bg-gray-500 checked:bg-blue-500 checked:bg-red-500 checked:bg-white checked:bg-green-500 checked:bg-orange-500 checked:bg-yellow-500" />
<div class="p-6">
  <div>
    <div class="overflow-x-auto whitespace-nowrap p-6 max-w-[39rem] mx-auto">
      {#each [
        ['', '', '', 'U1', 'U2', 'U3'],
        ['', '', '', 'U4', 'U5', 'U6'],
        ['', '', '', 'U7', 'U8', 'U9'],
        ['L1', 'L2', 'L3', 'F1', 'F2', 'F3', 'R1', 'R2', 'R3', 'B1', 'B2', 'B3'],
        ['L4', 'L5', 'L6', 'F4', 'F5', 'F6', 'R4', 'R5', 'R6', 'B4', 'B5', 'B6'],
        ['L7', 'L8', 'L9', 'F7', 'F8', 'F9', 'R7', 'R8', 'R9', 'B7', 'B8', 'B9'],
        ['', '', '', 'D1', 'D2', 'D3'],
        ['', '', '', 'D4', 'D5', 'D6'],
        ['', '', '', 'D7', 'D8', 'D9'],
        ] as row}
          {#each row as col}
            <button on:click={() => write(col)} disabled={!col} class={`w-10 h-10 rounded mx-1 my-0.5 bg-${cube[col] != undefined ? colors[cube[col]] : 'gray-500'} disabled:bg-transparent`} />
          {/each}
          <br />
        {/each}
    </div>
    <div class="mt-3 flex gap-2 justify-center">
      {#each colors as color, i}
        <input type="radio" name="color" bind:group={radioValue} value={i} disabled={Object.values(cube).filter(val => val == i).length > 8} class={`w-12 h-12 rounded radio bg-${color} checked:bg-${color}`} />
      {/each}
    </div>
  </div>
  <div class="mt-3 text-center">
    {cubestr}
  </div>
  <button on:click={solve} disabled={cubestr.length != 54} class="btn btn-primary w-full max-w-xs block mx-auto mt-3">Solve</button>
  <div class="mt-3 text-center">
    {result}
  </div>
</div>
