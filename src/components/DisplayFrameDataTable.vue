<template>
  <b-container>
    <b-row>
      <b-col>
        <div class="justify-content-md-center">
          <h1>{{ msg }}</h1>
        </div>
      </b-col>
    </b-row>
    <b-row>
      <b-col cols=2>
        <b-form-input v-model="filterCharacterOn" placeholder="Filter Out Character"></b-form-input>
      </b-col>
      <b-col cols=2>
        <b-form-input v-model="filterAttackOn" placeholder="Filter On Attack"></b-form-input>
      </b-col>
      <b-col cols=2>
        <b-form-input v-model="filterAttackOut" placeholder="Filter Out Attack"></b-form-input>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <b-table hover
                 :items="items" 
                 :fields="fields"
                 :filter="filters"
                 :filter-function="filterFunc">
        </b-table>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  data() {
    return {
      fields: [
        {
          key: 'Character',
          sortable: true
        },
        {
          key: 'Attack',
          sortable: true
        },
        {
          key: 'Damage',
          sortable: true
        },
        {
          key: 'Guard',
          sortable: true
        },
        {
          key: 'Startup',
          sortable: true
        },
        {
          key: 'Active',
          sortable: true
        },
        {
          key: 'Recovery',
          sortable: true
        },
        {
          key: 'On Block',
          sortable: true
        },
        {
          key: 'On Hit',
          sortable: true
        },
        'Level'
      ],
      items: [],
      filters: {
        filterAttackOn: '',
        filterAttackOut: '',
        filterCharacterOn: ''
      }
    }
  },
  name: 'HelloWorld',
  frameDataJSON: {},
  tableData: [],
  props: {
    msg: String
  },
  created() {
    this.getFrameDataJSON()
  },
  mounted() {
    this.items = this.tableData
  },
  computed: {
    filterAttackOn: {
      get(){
        return this.filters["filterAttackOn"]
      },
      set(newVal){
        return this.filters["filterAttackOn"] = newVal;
      }
    },
    filterAttackOut: {
      get(){
        return this.filters["filterAttackOut"]
      },
      set(newVal){
        return this.filters["filterAttackOut"] = newVal;
      }
    },
    filterCharacterOn: {
      get(){
        return this.filters["filterCharacterOn"]
      },
      set(newVal){
        return this.filters["filterCharacterOn"] = newVal;
      }
    }
  },
  methods: {
    getFrameDataJSON() {
      this.tableData = []
      this.frameDataJSON = require('../../character_frame_data.json')
      
      for (let [k, v] of Object.entries(this.frameDataJSON)) {
        for (var i in v) {
          for (let [j, m] of Object.entries(v[i])) {
            var c = {}
            c['Character'] = k
            c['Attack'] = j
            for (let [l, n] of Object.entries(m)) {  
              c[l] = n
            }
            this.tableData.push(c)
          }
        }
      }
    },
    filterFunc(row, filter) {
      if (filter["filterCharacterOn"].length > 0 && !row.Character.includes(filter["filterCharacterOn"])) {
        return false
      } else if (filter["filterAttackOn"].length > 0 && !row.Attack.includes(filter["filterAttackOn"])) {
        return false
      } else if (filter["filterAttackOut"].length > 0 && row.Attack.includes(filter["filterAttackOut"])) {
        return false
      }

      return true
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
