<template>
    <div>
        {{ getMovie }}
        {{ getMovie.rating_set }}
        <sweet-modal ref="modal">
            <sweet-modal-tab title="좋아요" id="tab1">
                <!-- <button v-show="rating.likes" @click.prevent="likesChange"><i class="heart outline icon"></i></button>
                <button v-show="!rating.likes" @click.prevent="likesChange"><i class="heart icon"></i></button> -->
                <button v-show="rating.likes" @click="likesChange">좋아요</button>
                <button v-show="!rating.likes" @click="likesChange">싫어요</button>
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
            <!-- icons is an object containing SVG strings -->
        </sweet-modal>
        <span v-show="!isValued" @click="open">평가하기</span>
        <span v-show="isValued" @click="open">수정하기</span>
        <button type="submit" @click="deleterating(rating)">삭제하기</button>
        <button v-show="!togglewish" type="submit" @click.prevent="addwishlist(rating.movieid)" @click="toggleWish">Wish</button>
        <button v-show="togglewish" type="submit" @click.prevent="deletewish(rating.movieid)" @click="toggleWish">취소</button>
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
            if (this.isValued) {
                this.rating.ratingid = this.getRatings[this.isValued-1].id
            }
        }
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
        }
    },
    created () {
        this.getmoviedetail(this.getMovieid);
        this.rating.movieid = this.getMovieid
        this.getRatingid();
    }
}
</script>

<style>

</style>