FROM node:16

WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install all dependencies, including dev dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Expose the port the app runs on
EXPOSE 5173

# Command to run the application
CMD ["npm", "run", "dev", "--", "--host"]