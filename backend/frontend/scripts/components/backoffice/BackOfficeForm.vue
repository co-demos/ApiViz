<template>
  <div 
    class="card"
    >
    
    <div class="card-header">
      <a 
        class="card-header-title"
        @click="toggleContent"
        >
        {{ fieldConfig.field }}
      </a>
      <a href="#" class="card-header-icon" aria-label="more options">
        <span class="icon">
          <i class="fas fa-angle-down" aria-hidden="true"></i>
        </span>
      </a>
    </div>

    <div 
      v-if="isOpen"
      class="card-content"
      >

      <div class="content">

        <!-- DEBUG -->
        fieldConfig : <code>{{ fieldConfig }}</code><br>
        config[fieldConfig.field] : <code>{{ config[fieldConfig.field] }}</code><br>
        <hr>

        <div
          v-for="conf in fieldConfig.edit" 
          >

          <!-- text field -->
          <div
            v-if="conf.type === 'text'" 
            class="field">
            <label class="label">{{conf.subfield}}</label>
            <div class="control">
              <input 
                :value="config[fieldConfig.field][conf.subfield]"
                class="input" 
                type="text" 
                placeholder="Text input"
                >
            </div>
            <p class="help">
              {{ config[fieldConfig.field]['help'] }}
            </p>
          </div>

          <!-- select field -->
          <div
            v-if="conf.type === 'select'" 
            class="field">
            <label class="label">Subject</label>
            <div class="control">
              <div class="select">
                <select>
                  <option>Select dropdown</option>
                  <option>With options</option>
                </select>
              </div>
            </div>
          </div>

          <!-- textarea field -->
          <div
            v-if="conf.type === 'textarea'" 
            class="field">
            <label class="label">Message</label>
            <div class="control">
              <textarea class="textarea" placeholder="Textarea"></textarea>
            </div>
          </div>

          <!-- check field -->
          <div
            v-if="conf.type === 'check'" 
            class="field">
            <div class="control">
              <label class="checkbox">
                <input type="checkbox">
                I agree to the <a href="#">terms and conditions</a>
              </label>
            </div>
          </div>

          <!-- radio field -->
          <div
            v-if="conf.type === 'radio'" 
            class="field">
            <div class="control">
              <label class="radio">
                <input type="radio" name="question">
                Yes
              </label>
              <label class="radio">
                <input type="radio" name="question">
                No
              </label>
            </div>
          </div>

          <br> 
        </div>
        

        <!-- SUBMIT -->
        <div class="field is-grouped">
          <div class="control">
            <button class="button is-link">Submit</button>
          </div>
          <div class="control">
            <button class="button is-text">Cancel</button>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>

export default {
  components: {
  },
  props: [
    'fieldConfig',
    'config'
  ],
  data: function () {
    return {
      isOpen : false,
    }
  },
  computed : {

  },
  methods : {
    
    toggleContent() {
      this.isOpen = !this.isOpen
    },

  }
}
</script>

<style>

</style>