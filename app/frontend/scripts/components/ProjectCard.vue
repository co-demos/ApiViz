<template>
    <div class="column is-12">
        <div class="card proj-card">

            <router-link :to="`/${dataset_uri}/detail?id=${projectInfos.id}`" class="card-image">
                <img class="proj-card-img" :src="projectInfos.image" :alt="'illustration du projet' + projectInfos.title" >
            </router-link>

            <div class="card-content">
                <div class="content" v-if="projectInfos.address">
                    <span class="icon">
                        <img class="image is-16x16" src="/static/icons/icon_pin.svg">
                    </span>
                    <span class="subtitle is-6">
                        {{projectInfos.address}}
                    </span>
                </div>

                <p class="title is-5">
                    <router-link :to="`/${dataset_uri}/detail?id=${projectInfos.id}`">
                        {{projectInfos.title}}
                    </router-link>
                </p>

                <div class="content">
                    <p class="subtitle is-6">{{projectInfos.summary}}</p>
                </div>

                <div class="content" v-if="Array.isArray(projectInfos.tags) && projectInfos.tags.length >=1">
                    <span v-for="tag in projectInfos.tags" class="tag" :key="tag">
                        {{tag}}
                    </span>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
import { mapState } from "vuex";

const MAX_SUMMARY_LENGTH = 120;

export default {
    components: {},

    props: ["project"],

    computed: {
        summary(){
            const {description = '(projet sans résumé)'} = this.project

            const tail = description.length > MAX_SUMMARY_LENGTH ? '...' : '';

            return description.slice(0, MAX_SUMMARY_LENGTH) + tail
        },
        dataset_uri(){
          return this.$store.state.search.dataset_uri
        },
        projectInfos(){
          return this.$store.getters.getProjectConfigUniform(this.project)
        },
    }
};
</script>

<style lang="scss" scoped>
@import '../../styles/apiviz-misc.scss';

.card-image {
    min-height: 100px;
}

.card-image img{
    width: 100%;
}

.proj-card {
	border-radius: 3px ;
	box-shadow : $apiviz-discrete-shadow;
}

.proj-card-img {
	border-radius : 3px 3px 0px 0px ;
}

.card-content .tag{
    margin-right: 0.5em;
    margin-bottom: 0.5em;

    padding: 0.2em 1em;

    background-color: #767676;
    color: white;

    font-size: 12px;
}

.card-content img{
    max-height: 1.1em;
    transform: translateY(0.1em);
}

</style>
