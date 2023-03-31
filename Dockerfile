FROM python:3.7.5
# Update the system
RUN apt-get update && apt-get upgrade -y
# Copy get-poetry.py
COPY get-poetry.py /tmp/get-poetry.py
COPY pyproject.toml pyproject.toml
# Install poetry
RUN python3 /tmp/get-poetry.py
# Set the path
ENV PATH="/root/.local/bin:${PATH}"
# Add poetry path to bash and update poetry
RUN echo 'export PATH="/root/.local/bin:$PATH"' >> ~/.bashrc
# Expose port
EXPOSE 8080
WORKDIR /BiOrbit_data
# Copy folder
COPY . /BiOrbit_data/
RUN poetry update
# bash
CMD ["bash"]
