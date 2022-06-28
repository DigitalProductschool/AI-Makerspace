# lightweight python
FROM python:3.8-slim

RUN apt-get update \
    && apt-get install --yes --no-install-recommends

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN ls -la $APP_HOME/

# if we have a packages.txt, install it
COPY packages.txt packages.txt
RUN xargs -a packages.txt apt-get install --yes

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Run the streamlit on container startup
CMD [ "streamlit", "run","streamlit_app.py" ]
