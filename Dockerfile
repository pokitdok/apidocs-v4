FROM ruby:2.1.5

WORKDIR /app
ADD Gemfile* /app/
RUN bundle install
