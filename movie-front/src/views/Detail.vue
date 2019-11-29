<template>
    <div class="ui main container">
        <h1 class="ui header">{{ getMovie.title }}</h1>
        <p>{{ getMovie.titleEng }}</p>
        <img :src="getMovie.poster" :alt="getMovie.title">
    <h4 class="ui horizontal divider header">
        <i class="bar chart icon"></i>
        Movie Information
    </h4>
    <table class="ui definition table">
    <tbody>
        <tr>
        <td class="two wide column">Director</td>
        <td>{{ getMovie.director }}</td>
        </tr>
        <tr>
        <td>Actors</td>
        <td>{{ getMovie.actors }}</td>
        </tr>
        <tr>
        <td>Plot</td>
        <td>{{ getMovie.plot }}</td>
        </tr>
        <tr>
        <td>Descriptions</td>
        <td>{{ getMovie.descriptions }}</td>
        </tr>
        <tr>
        <td>Nation</td>
        <td>{{ getMovie.nation }}</td>
        </tr>
        <tr>
        <td>Runtime</td>
        <td>{{ getMovie.runtime }}</td>
        </tr>
        <tr>
        <td>Rating Grade</td>
        <td>{{ getMovie.ratingGrade }}</td>
        </tr>
        <tr>
        <td>Release Date</td>
        <td>{{ getMovie.releaseDt }}</td>
        </tr>
    </tbody>
    </table>
        <b-button v-b-modal.modal-center>Stills</b-button>
        <div>
            <b-modal id="modal-center" centered :title="getMovie.title">
                <b-carousel
                id="carousel-fade"
                style="text-shadow: 0px 0px 2px #000"
                fade
                indicators
                img-width="1024"
                img-height="480"
                >
                <b-carousel-slide v-for="still in stills" :key="still.id"
                :img-src="still"
                ></b-carousel-slide>
                </b-carousel> 
                <template v-slot:modal-footer="{ cancel }">
                    <b-button size="sm" variant="danger" @click="cancel()">
                        닫기
                    </b-button>
                </template>
            </b-modal>
        </div>
        <div class="ui comments center">
            <h3 class="ui dividing header">Reviews</h3>
            <div class="comment" v-for="rate in getMovie.rating_set" :key="rate.id">
                <a v-show="!rating.like"><i class="heart outline icon"></i></a>
                <a v-show="rating.like"><i class="heart icon"></i></a>
                <div class="content">
                    <div class="text">
                        {{ rate.comment }}
                    </div>
                </div>
                <button class="ui button" v-show="getUserpk==rate.user" type="submit" @click="getRatingid(rating.id)" @click.prevent="deleterating(rating)">삭제</button>
            </div>
        </div>
        <sweet-modal ref="modal">
            <sweet-modal-tab title="좋아요" id="tab1">
                <a v-show="!rating.likes" @click.prevent="likesChange"><i class="heart outline icon"></i></a>
                <a v-show="rating.likes" @click.prevent="likesChange"><i class="heart icon"></i></a>
            </sweet-modal-tab>
            <sweet-modal-tab title="키워드" id="tab2">
                <div>
                    <select name="keyword1" id="" v-model="rating.keyword1">
                        <option value="1">키덜트</option>
                        <option value="2">히어로</option>
                        <option value="3">매력적인 캐릭터</option>
                        <option value="4">원작을 재해석한</option>
                        <option value="5">탄탄한 스토리</option>
                        <option value="6">영상미 넘치는</option>
                        <option value="7">OST가 좋은</option>
                        <option value="8">작품성이 좋은</option>
                        <option value="9">연기력</option>
                        <option value="10">심오한</option>
                        <option value="11">웅장한</option>
                        <option value="12">잔인한</option>
                        <option value="13">다양성</option>                        
                        <option value="14">연애세포를 깨워줄</option>
                        <option value="15">향수를 불러일으키는</option>
                        <option value="16">잔잔한</option>
                        <option value="17">충격적인</option>
                        <option value="18">반전있는</option>
                        <option value="19">감동적인</option>
                        <option value="20">여운이 남는</option>
                        <option value="21">화끈한</option>
                        <option value="22">오글거리는</option>
                        <option value="23">감성적인</option>                                                                      
                    </select>
                </div>
                <div>
                    <select name="keyword2" id="" v-model="rating.keyword2">
                        <option value="1">키덜트</option>
                        <option value="2">히어로</option>
                        <option value="3">매력적인 캐릭터</option>
                        <option value="4">원작을 재해석한</option>
                        <option value="5">탄탄한 스토리</option>
                        <option value="6">영상미 넘치는</option>
                        <option value="7">OST가 좋은</option>
                        <option value="8">작품성이 좋은</option>
                        <option value="9">연기력</option>
                        <option value="10">심오한</option>
                        <option value="11">웅장한</option>
                        <option value="12">잔인한</option>
                        <option value="13">다양성</option>                        
                        <option value="14">연애세포를 깨워줄</option>
                        <option value="15">향수를 불러일으키는</option>
                        <option value="16">잔잔한</option>
                        <option value="17">충격적인</option>
                        <option value="18">반전있는</option>
                        <option value="19">감동적인</option>
                        <option value="20">여운이 남는</option>
                        <option value="21">화끈한</option>
                        <option value="22">오글거리는</option>
                        <option value="23">감성적인</option>                                                                    
                    </select>
                </div>    
            </sweet-modal-tab>
            <sweet-modal-tab title="한줄평" id="tab3">
                <input type="text" name="" id="" v-model="rating.comment">
                <button v-show="!isValued" type="submit" @click.prevent="sendRating(rating)">등록</button>
                <button v-show="isValued" type="submit" @click.prevent="updateRating(rating)">수정</button>                
            </sweet-modal-tab>
        </sweet-modal>
        <div class="ui basic buttons">
            <span class="ui button" v-show="!isValued" @click="open">평가하기</span>
            <span class="ui button" v-show="isValued" @click="open">수정하기</span>
            <button class="ui button" v-show="!togglewish" type="submit" @click.prevent="addwishlist(rating.movieid)" @click="toggleWish">Wish</button>
            <button class="ui button" v-show="togglewish" type="submit" @click.prevent="deletewish(rating.movieid)" @click="toggleWish">취소</button>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { SweetModal, SweetModalTab } from 'sweet-modal-vue'
export default {
    name: 'detail',
    components: {
        SweetModal,
        SweetModalTab
    },
    data () {
        return {
            togglewish: false,
            rating: {
                movieid: 0,
                ratingid: 0,
                likes: false,
                comment: '',
                keyword1: 0,
                keyword2: 0
            }
        }
    },
    methods: {
        ...mapActions(['sendRating', 'getmoviedetail', 'updateRating', 'deleterating', 'addwishlist', 'deletewish']),
        open () {
            return this.$refs.modal.open()
        },
        close () {
            return this.$refs.modal.close()
        },
        likesChange () {
            if (this.rating.likes) {
                this.rating.likes = false
            } else {
                this.rating.likes = true
            }
        },
        toggleWish () {
            this.togglewish = !this.togglewish
        },
        getRatingid () {
            const idx = this.isValued-1
            this.rating.ratingid = this.getRatings[idx].id
        },
    },
    computed: {
        ...mapGetters(['getMovie','getUserpk', 'getMovieid', 'getRatingcount', 'getRatings']),
        isValued () {
            let flag = 0
            for (let i=0; i < this.getRatingcount; i++) {
                if (this.getRatings[i].user == this.getUserpk) {
                    flag = i+1
                    return flag
                }
            }
            return flag
        },
        stills () {
            return this.getMovie.stills.split('|')
        }
    },
    created () {
        const movieid = sessionStorage.getItem('movie')
        this.getmoviedetail(movieid);
        this.rating.movieid = movieid
        this.getRatingid();
    }
}
</script>

<style>

</style>