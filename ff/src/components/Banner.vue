<template>
    <div class="banner-carousel">
      <div class="carousel-container">
        <div class="carousel-track" :style="trackStyle">
          <div
            class="carousel-slide"
            v-for="(image, index) in images"
            :key="index"
          >
            <img :src="image" :alt="'Banner ' + (index + 1)">
          </div>
        </div>

        <button class="carousel-nav prev" @click="prevSlide">‹</button>
        <button class="carousel-nav next" @click="nextSlide">›</button>

        <div class="carousel-dots">
          <button
            v-for="(dot, index) in images"
            :key="index"
            @click="goToSlide(index)"
            :class="{ active: currentIndex === index }"
          ></button>
        </div>
      </div>
    </div>
  </template>

  <script>
  export default {
    name: 'BannerCarousel',
    props: {
      images: {
        type: Array,
        required: true,
        validator: value => value.length >= 2 && value.length <= 3
      },
      interval: {
        type: Number,
        default: 5000
      }
    },
    data() {
      return {
        currentIndex: 0,
        timer: null
      }
    },
    computed: {
      trackStyle() {
        return {
          transform: `translateX(-${this.currentIndex * 100}%)`
        }
      }
    },
    mounted() {
      this.startAutoPlay()
    },
    beforeUnmount() {
      this.stopAutoPlay()
    },
    methods: {
      startAutoPlay() {
        this.timer = setInterval(() => {
          this.nextSlide()
        }, this.interval)
      },
      stopAutoPlay() {
        if (this.timer) {
          clearInterval(this.timer)
          this.timer = null
        }
      },
      nextSlide() {
        this.currentIndex = (this.currentIndex + 1) % this.images.length
      },
      prevSlide() {
        this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length
      },
      goToSlide(index) {
        this.currentIndex = index
      }
    }
  }
  </script>

  <style scoped>
  .banner-carousel {
    margin-top: 50px;
    width: 100%;
    overflow: hidden;
  }

  .carousel-container {
    position: relative;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    overflow: hidden;
  }

  .carousel-track {
    display: flex;
    transition: transform 0.5s ease;
  }

  .carousel-slide {
    min-width: 100%;
    box-sizing: border-box;
  }

  .carousel-slide img {
    width: 100%;
    height: auto;
    max-height: 400px;
    object-fit: cover;
    border-radius: 8px;
  }

  .carousel-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(255, 255, 255, 0.5);
    border: none;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    font-size: 24px;
    cursor: pointer;
    z-index: 10;
  }

  .carousel-nav.prev {
    left: 10px;
  }

  .carousel-nav.next {
    right: 10px;
  }

  .carousel-dots {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 8px;
  }

  .carousel-dots button {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    border: none;
    background: rgba(255, 255, 255, 0.5);
    cursor: pointer;
    padding: 0;
  }

  .carousel-dots button.active {
    background: white;
  }

  @media (max-width: 768px) {
    .banner-carousel {
      margin-top: 70px;
    }

    .carousel-slide img {
      max-height: 300px;
    }
  }

  @media (max-width: 480px) {
    .banner-carousel {
      margin-top: 60px;
    }

    .carousel-slide img {
      max-height: 200px;
    }

    .carousel-nav {
      width: 30px;
      height: 30px;
      font-size: 18px;
    }
  }
  </style>
