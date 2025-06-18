<script setup lang="ts">
// import { useDate } from 'vuetify'
import SelectDate from '@/views/option/select_date.vue'
import { ref } from 'vue'
// const date = useDate()
// date.locale = 'zhHans'
// console.log(date)
// const format = date.date(Date.now())
// console.log(format)
const switchDialog = ref(false)

const touchSelectDate = () => {
  switchDialog.value = true
}

</script>

<template>
<div
  class="v_option_profit_calculation"
>
  <div
    class="container"
  >
    <div
      class="future_wrapper"
    >
      <div
        class="title_wrapper mb-5"
      >
        <div
          class="title text-h6"
        >
          Future Config
        </div>
      </div>
      <div
        class="future_group d-flex"
      >
        <v-select
          class="future_select"
          label="Select Future"
          density="compact"
          :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"
          variant="solo"
          width="200px"
          max-width="300px"
        ></v-select>
        <v-select
          class="future_select ml-5"
          label="Select Contract"
          density="compact"
          :items="['2507', '2508', '2509', '2510', '2511', '2512']"
          variant="solo"
          width="200px"
          max-width="300px"
        ></v-select>
        <v-btn
          color="primary"
          class="ml-5"
          variant="tonal"
        >
          Sure
        </v-btn>
      </div>
    </div>
    <div
      class="time_wrapper"
    >
      <div
        class="title text-h6"
      >
        Time Config
      </div>
      <div
        class="time_range_wrapper d-flex algin-center"
      >
        <div
          class="time_range_group d-flex align-center"
        >
          <v-text-field
            label="Starting"
            density="compact"
            variant="solo"
            :hide-details="true"
          ></v-text-field>
          <v-btn
            class="ml-5"
            @click="touchSelectDate"
          >
            Select
          </v-btn>
        </div>
        <div
          class="time_range_group d-flex align-center ml-10"
        >
          <v-text-field
            label="Ending"
            density="compact"
            variant="solo"
            :hide-details="true"
          ></v-text-field>
          <v-btn
            class="ml-5"
          >
            Select
          </v-btn>
        </div>

      </div>
      <div
        class="time_group"
      >

        <div
          class="range_silder_group"
        >
          <v-range-slider></v-range-slider>
        </div>
      </div>
    </div>
  </div>
  <SelectDate
    :switch-dialog="switchDialog"
  ></SelectDate>

</div>
</template>

<style scoped>
.v_option_profit_calculation {
  width: 100%;
  background-color: #fcfcfc;
  .container {
    width: 100%;
    padding: 20px;
    max-width: 1200px;
    margin: 0 auto;
    background-color: #fff;
  }
  .future_wrapper {
    .future_group {
      .future_select {
        width: 200px;
        font-size: 12px;
      }
    }
  }
  .time_wrapper {
    .time_range_wrapper {
      .time_range_group {
        width: 400px;

      }
    }
  }
}
</style>
